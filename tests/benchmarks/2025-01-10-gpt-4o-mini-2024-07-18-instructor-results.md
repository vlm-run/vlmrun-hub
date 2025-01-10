## Benchmark Results (model=gpt-4o-mini-2024-07-18, date=2025-01-10)

<table>
<tr>
<td style='width: 5%;'> Domain </td>
<td style='width: 5%;'> Response Model </td>
<td style='width: 40%;'> Sample </td>
<td style='width: 50%;'> Response JSON </td>
</tr>
    <tr><td> <kbd>document.invoice</kbd> </td>
<td> <kbd>Invoice</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.invoice/invoice_1.jpg' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.receipt</kbd> </td>
<td> <kbd>Receipt</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.receipt/sample_receipt.webp' width='100%' /> </td>
<td> <pre>{<br>  "receipt_id": null,<br>  "transaction_date": "2021-01-26T22:36:22",<br>  "merchant_name": "Walmart",<br>  "merchant_address": {<br>    "street": "8060 W TROPICAL PKWY",<br>    "city": "LAS VEGAS",<br>    "state": "NV",<br>    "postal_code": "89149",<br>    "country": null<br>  },<br>  "merchant_phone": null,<br>  "cashier_name": "SARAH",<br>  "register_number": "35",<br>  "customer_name": null,<br>  "customer_id": null,<br>  "items": [<br>    {<br>      "description": "BOYS CREW",<br>      "quantity": 1.0,<br>      "unit_price": 9.48,<br>      "total_price": 9.48<br>    },<br>    {<br>      "description": "BOYS SOCKS",<br>      "quantity": 1.0,<br>      "unit_price": 6.97,<br>      "total_price": 6.97<br>    },<br>    {<br>      "description": "BOXER BRIEF",<br>      "quantity": 1.0,<br>      "unit_price": 10.98,<br>      "total_price": 10.98<br>    }<br>  ],<br>  "subtotal": 27.43,<br>  "tax": 2.3,<br>  "total": 29.73,<br>  "currency": "USD",<br>  "payment_method": {<br>    "type": "Debit",<br>    "card_last_4": "****",<br>    "card_type": null<br>  },<br>  "discount_amount": null,<br>  "discount_description": null,<br>  "tip_amount": null,<br>  "return_policy": null,<br>  "barcode": null,<br>  "additional_charges": null,<br>  "notes": null,<br>  "others": null<br>}</pre> </td>
</tr><tr><td> <kbd>document.resume</kbd> </td>
<td> <kbd>Resume</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.resume/fake-resume.webp' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.us-drivers-license</kbd> </td>
<td> <kbd>USDriversLicense</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.us-drivers-license/dl3.jpg' width='100%' /> </td>
<td> <pre>{<br>  "issuing_state": "MT",<br>  "license_number": "0812319684104",<br>  "full_name": "Brenda Lynn Sample",<br>  "first_name": "Brenda",<br>  "middle_name": "Lynn",<br>  "last_name": "Sample",<br>  "address": {<br>    "street": "123 MAIN STREET",<br>    "city": "HELENA",<br>    "state": "MT",<br>    "zip_code": "59601"<br>  },<br>  "date_of_birth": "1968-08-04",<br>  "gender": "F",<br>  "height": "5'06\"",<br>  "weight": 150.0,<br>  "eye_color": "BRO",<br>  "hair_color": null,<br>  "issue_date": "2015-02-15",<br>  "expiration_date": "2023-08-04",<br>  "license_class": "D",<br>  "donor": null,<br>  "veteran": null<br>}</pre> </td>
</tr><tr><td> <kbd>document.utility-bill</kbd> </td>
<td> <kbd>UtilityBill</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.utility-bill/utility-bill-example.webp' width='100%' /> </td>
<td> <pre>{<br>  "account_number": "1234567890-1",<br>  "date_mailed": "2019-09-07",<br>  "service_for": "SPARKY JOULE",<br>  "service_address": {<br>    "street": "12345 ENERGY CT",<br>    "city": null,<br>    "state": null,<br>    "zip_code": null<br>  },<br>  "billing_period_start": null,<br>  "billing_period_end": null,<br>  "date_due": "2019-09-28",<br>  "amount_due": 88.14,<br>  "previous_balance": 0.0,<br>  "payment_received": 91.57,<br>  "current_charges": 88.14,<br>  "breakdown_of_charges": [<br>    {<br>      "description": "Current PG&E Electric Delivery Charges",<br>      "amount": 55.66,<br>      "usage": null,<br>      "rate": null<br>    },<br>    {<br>      "description": "Silicon Valley Clean Energy Electric Generation Charges",<br>      "amount": 32.48,<br>      "usage": null,<br>      "rate": null<br>    }<br>  ],<br>  "payment_options": [<br>    "www.pge.com/waystopay"<br>  ],<br>  "contact_information": {<br>    "phone": "1-800-743-5000",<br>    "website": "www.pge.com/MyEnergy"<br>  }<br>}</pre> </td>
</tr><tr><td> <kbd>document.w2-form</kbd> </td>
<td> <kbd>W2Form</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.w2-form/w2-form.jpg' width='100%' /> </td>
<td> <pre>{<br>  "control_number": "GNI851",<br>  "ein": "63-0065650",<br>  "ssn": "554-03-0876",<br>  "employee_name": "Anastasia Hodges",<br>  "employee_address": {<br>    "street": "200 2nd Street NE",<br>    "city": "Waseca",<br>    "state": "MN",<br>    "zip_code": "56093"<br>  },<br>  "employer_name": "NORTH 312",<br>  "employer_address": {<br>    "street": "151 N Market Street",<br>    "city": "Wooster",<br>    "state": "OH",<br>    "zip_code": "44691"<br>  },<br>  "wages_tips_other_compensation": 23677.7,<br>  "federal_income_tax_withheld": 2841.32,<br>  "social_security_wages": 24410.0,<br>  "social_security_tax_withheld": 1513.42,<br>  "medicare_wages_and_tips": 24410.0,<br>  "medicare_tax_withheld": 353.95,<br>  "tax_year": 2020<br>}</pre> </td>
</tr><tr><td> <kbd>aerospace.remote-sensing</kbd> </td>
<td> <kbd>RemoteSensing</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/aerospace.remote-sensing/planet_labs_port.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": "The satellite image captures a coastal urban area adjacent to a busy port. The scene includes residential neighborhoods, a marina, and extensive shipping facilities with numerous cargo containers visible. The waterway is active with vessels, indicating significant maritime activity.",<br>  "objects": [<br>    "residential buildings",<br>    "marina",<br>    "cargo containers",<br>    "shipping docks",<br>    "waterway",<br>    "roads",<br>    "beach"<br>  ],<br>  "categories": [<br>    "commercial-area",<br>    "port",<br>    "residential-area",<br>    "water-treatment",<br>    "beach"<br>  ],<br>  "is_visible": true<br>}</pre> </td>
</tr><tr><td> <kbd>healthcare.medical-insurance-card</kbd> </td>
<td> <kbd>MedicalInsuranceCard</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/healthcare.medical-insurance-card/blue_cross_example.jpg' width='100%' /> </td>
<td> <pre>{<br>  "provider_service": {<br>    "provider_service_number": null,<br>    "precertification_number": null<br>  },<br>  "member_information": {<br>    "member_name": "Member Name",<br>    "member_id": "XY2 123456789",<br>    "group_number": "023457"<br>  },<br>  "pharmacy_plan": {<br>    "rx_bin": "987654",<br>    "rx_pcn": null,<br>    "rx_grp": "HIOPT",<br>    "pharmacy_help_desk": null<br>  },<br>  "insurance_provider": {<br>    "provider_name": "BlueCross BlueShield",<br>    "network": "PPO"<br>  },<br>  "coverage": {<br>    "office_visit": "$15",<br>    "specialist_visit": null,<br>    "urgent_care": null,<br>    "emergency_room": "$75",<br>    "inpatient_hospital": null<br>  }<br>}</pre> </td>
</tr><tr><td> <kbd>retail.ecommerce-product-caption</kbd> </td>
<td> <kbd>RetailEcommerceProductCaption</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/retail.ecommerce-product-caption/Electronics%20-%20Kindle.webp' width='100%' /> </td>
<td> <pre>{<br>  "description": "The Kindle Paperwhite features a 6.8\" display and adjustable warm light for a comfortable reading experience. It is designed for easy portability and offers a sleek black finish.",<br>  "rating": 85,<br>  "name": "Kindle Paperwhite",<br>  "brand": "Amazon",<br>  "category": "Electronics / E-readers",<br>  "price": "$139.99",<br>  "color": "Black"<br>}</pre> </td>
</tr><tr><td> <kbd>media.tv-news</kbd> </td>
<td> <kbd>TVNews</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.tv-news/bbc_news_ukraine_screenshot.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": "A news anchor presenting a segment about President Biden criticizing Netanyahu in an interview.",<br>  "chyron": "Biden criticises Netanyahu in an interview",<br>  "network": "BBC News",<br>  "reporters": null<br>}</pre> </td>
</tr><tr><td> <kbd>media.nfl-game-state</kbd> </td>
<td> <kbd>NFLGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nfl-game-state/packers_cardinals_screenshot.png' width='100%' /> </td>
<td> <pre>{<br>  "description": null,<br>  "teams": [<br>    {<br>      "name": "GB",<br>      "score": 0<br>    },<br>    {<br>      "name": "AZ",<br>      "score": 7<br>    }<br>  ],<br>  "status": "in_progress",<br>  "quarter": 2,<br>  "clock_time": "12:12",<br>  "possession_team": "GB",<br>  "down": "2nd",<br>  "distance": 10,<br>  "yard_line": -10,<br>  "network": "NBC",<br>  "is_shown": true<br>}</pre> </td>
</tr><tr><td> <kbd>media.nba-game-state</kbd> </td>
<td> <kbd>NBAGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nba-game-state/heats_spurs.png' width='100%' /> </td>
<td> <pre>{<br>  "description": null,<br>  "teams": [<br>    {<br>      "name": "MIA",<br>      "score": 7<br>    },<br>    {<br>      "name": "SA",<br>      "score": 6<br>    }<br>  ],<br>  "status": "in_progress",<br>  "quarter": 1,<br>  "clock_time": "9:09",<br>  "shot_clock": 11,<br>  "network": "ESPN",<br>  "is_shown": true<br>}</pre> </td>
</tr>
</table>
