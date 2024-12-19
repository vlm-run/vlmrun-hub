from io import BytesIO
from pathlib import Path
from typing import Literal, Union

import requests
from PIL import Image
from base64 import b64encode

VLMRUN_CACHE_DIR = Path.home() / ".vlmrun" / "cache"
VLMRUN_HUB_DIR = Path.home() / ".vlmrun" / "hub"

VLMRUN_HUB_DIR.mkdir(parents=True, exist_ok=True)
VLMRUN_CACHE_DIR.mkdir(parents=True, exist_ok=True)


def encode_image(
    image: Union[Image.Image, str, Path],
    format: Literal["PNG", "JPEG", "binary"] = "JPEG",
    quality: int = 98,
) -> Union[str, bytes]:
    """Convert an image to a base64 string."""
    if isinstance(image, (str, Path)):
        if not Path(image).exists():
            raise FileNotFoundError(f"File not found {image}")
        image = Image.open(str(image)).convert("RGB")
    elif isinstance(image, Image.Image):
        image = image.convert("RGB")
    else:
        raise ValueError(f"Invalid image type: {type(image)}")

    buffered = BytesIO()
    if format == "binary":
        image.save(buffered, format="PNG")
        buffered.seek(0)
        return buffered.getvalue()

    image_format = image.format or format
    image.save(buffered, format=image_format, subsampling=0, quality=quality)
    img_str = b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/{image_format.lower()};base64,{img_str}"


_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}


def remote_image(url: str | Path) -> Image.Image:
    assert isinstance(
        url, (str, Path)
    ), f"Invalid type for url [url={url}, type={type(url)}]"
    if url.startswith("http"):
        bytes = requests.get(url, headers=_HEADERS).content
        return Image.open(BytesIO(bytes)).convert("RGB")
    elif isinstance(url, Path):
        return Image.open(url).convert("RGB")
    else:
        raise ValueError(f"Invalid url type [url={url}, type={type(url)}]")
