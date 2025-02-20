from collections import namedtuple
from datetime import datetime
from pathlib import Path

import pytest
from loguru import logger


def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="document.us-drivers-license", help="Domain to test")


@pytest.fixture
def domain_arg(request):
    """Domain fixture for testing"""
    return request.config.getoption("--domain")


BenchmarkResult = namedtuple("BenchmarkResult", ["domain", "sample", "response_model", "response_json"])


def create_benchmark(results: list[BenchmarkResult], model: str, suffix: str):
    # Write the results to a pandas dataframe -> HTML
    # render the data_url in a new column
    BENCHMARK_DIR = Path(__file__).parent / "benchmarks"
    BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    benchmark_path = BENCHMARK_DIR / f"{date_str}-{model}-{suffix}-results.md".replace("/", "-")

    # Render the results in markdown
    def parse_json(x):
        return x.replace("\n", "<br>") if x is not None else "❌"

    markdown_str = f"## Benchmark Results (model={model}, date={date_str})\n\n"
    markdown_str += """<table>
<tr>
<td style='width: 5%;'> Domain </td>
<td style='width: 5%;'> Response Model </td>
<td style='width: 40%;'> Sample </td>
<td style='width: 50%;'> Response JSON </td>
</tr>
    """
    for result in results:
        markdown_str += "<tr>"
        markdown_str += f"<td> <kbd>{result.domain}</kbd> </td>\n"
        markdown_str += f"<td> <kbd>{result.response_model}</kbd> </td>\n"
        markdown_str += f"<td> <img src='{result.sample}' width='100%' /> </td>\n"
        markdown_str += "<td> <pre>{x}</pre> </td>\n".format(x=parse_json(result.response_json))
        markdown_str += "</tr>"
    markdown_str += "\n</table>"

    with benchmark_path.open("w") as f:
        f.write(markdown_str)
    logger.debug(f"Results written to {benchmark_path}")
