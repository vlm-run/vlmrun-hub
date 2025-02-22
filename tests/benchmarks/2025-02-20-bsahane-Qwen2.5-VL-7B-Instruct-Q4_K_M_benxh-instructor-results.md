## Benchmark Results (model=bsahane/Qwen2.5-VL-7B-Instruct:Q4_K_M_benxh, date=2025-02-20)

<table>
<tr>
<td style='width: 5%;'> Domain </td>
<td style='width: 5%;'> Response Model </td>
<td style='width: 40%;'> Sample </td>
<td style='width: 50%;'> Response JSON </td>
</tr>
    <tr><td> <kbd>document.bank-statement</kbd> </td>
<td> <kbd>BankStatement</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.bank-statement/lending_bankstatement.pdf' width='100%' /> </td>
<td> <pre>{<br>  "account_number": null,<br>  "account_type": null,<br>  "bank_address": null,<br>  "bank_name": null,<br>  "client_address": null,<br>  "client_name": null,<br>  "ending_balance": null,<br>  "starting_balance": null,<br>  "statement_date": null,<br>  "statement_start_date": null,<br>  "statement_end_date": null,<br>  "table_item": [],<br>  "others": null<br>}</pre> </td>
</tr><tr><td> <kbd>document.invoice</kbd> </td>
<td> <kbd>Invoice</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.invoice/invoice_1.jpg' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.receipt</kbd> </td>
<td> <kbd>Receipt</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.receipt/sample_receipt.webp' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.resume</kbd> </td>
<td> <kbd>Resume</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.resume/fake-resume.webp' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.us-drivers-license</kbd> </td>
<td> <kbd>USDriversLicense</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.us-drivers-license/dl3.jpg' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.utility-bill</kbd> </td>
<td> <kbd>UtilityBill</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.utility-bill/utility-bill-example.webp' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.w2-form</kbd> </td>
<td> <kbd>W2Form</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.w2-form/w2-form.jpg' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>aerospace.remote-sensing</kbd> </td>
<td> <kbd>RemoteSensing</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/aerospace.remote-sensing/planet_labs_port.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": "The satellite image shows an airport with visible runways and surrounding infrastructure, indicating a clear view from space.",<br>  "objects": [<br>    "runway"<br>  ],<br>  "categories": [<br>    "airport"<br>  ],<br>  "is_visible": true<br>}</pre> </td>
</tr><tr><td> <kbd>healthcare.medical-insurance-card</kbd> </td>
<td> <kbd>MedicalInsuranceCard</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/healthcare.medical-insurance-card/blue_cross_example.jpg' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>retail.ecommerce-product-caption</kbd> </td>
<td> <kbd>RetailEcommerceProductCaption</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/retail.ecommerce-product-caption/Electronics%20-%20Kindle.webp' width='100%' /> </td>
<td> <pre>{<br>  "description": "A sleek, modern e-reader with a vibrant display and intuitive interface.",<br>  "rating": 85,<br>  "name": "E-Reader Pro",<br>  "brand": "TechGenius",<br>  "category": "Electronics / E-readers",<br>  "price": "$299.99",<br>  "color": "Black"<br>}</pre> </td>
</tr><tr><td> <kbd>media.tv-news</kbd> </td>
<td> <kbd>TVNews</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.tv-news/bbc_news_ukraine_screenshot.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": "[img-0]",<br>  "chyron": null,<br>  "network": null,<br>  "reporters": []<br>}</pre> </td>
</tr><tr><td> <kbd>document.us-passport</kbd> </td>
<td> <kbd>USPassport</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.us-passport/2020-Next-Gen-US-Passport.png' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>media.nfl-game-state</kbd> </td>
<td> <kbd>NFLGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nfl-game-state/packers_cardinals_screenshot.png' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>media.nba-game-state</kbd> </td>
<td> <kbd>NBAGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nba-game-state/heats_spurs.png' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr>
</table>
