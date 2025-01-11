## Benchmark Results (model=phi4, date=2025-01-11)

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
<td> <pre>{<br>  "invoice_id": null,<br>  "period_start": null,<br>  "period_end": null,<br>  "invoice_issue_date": null,<br>  "invoice_due_date": null,<br>  "order_id": null,<br>  "customer_id": null,<br>  "issuer": null,<br>  "issuer_address": null,<br>  "customer": null,<br>  "customer_email": null,<br>  "customer_phone": null,<br>  "customer_billing_address": null,<br>  "customer_shipping_address": null,<br>  "items": null,<br>  "subtotal": null,<br>  "tax": null,<br>  "total": null,<br>  "currency": null,<br>  "notes": null<br>}</pre> </td>
</tr><tr><td> <kbd>document.receipt</kbd> </td>
<td> <kbd>Receipt</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.receipt/sample_receipt.webp' width='100%' /> </td>
<td> <pre>{<br>  "receipt_id": null,<br>  "transaction_date": null,<br>  "merchant_name": null,<br>  "merchant_address": null,<br>  "merchant_phone": null,<br>  "cashier_name": null,<br>  "register_number": null,<br>  "customer_name": "John Doe",<br>  "customer_id": null,<br>  "items": [<br>    {<br>      "description": "Espresso Coffee",<br>      "quantity": 2.0,<br>      "unit_price": 3.5,<br>      "total_price": 7.0<br>    },<br>    {<br>      "description": "Blueberry Muffin",<br>      "quantity": 1.0,<br>      "unit_price": 2.75,<br>      "total_price": 2.75<br>    }<br>  ],<br>  "subtotal": 9.75,<br>  "tax": 0.78,<br>  "total": 11.53,<br>  "currency": "USD",<br>  "payment_method": {<br>    "type": "Credit Card",<br>    "card_last_4": null,<br>    "card_type": null<br>  },<br>  "discount_amount": null,<br>  "discount_description": null,<br>  "tip_amount": 1.0,<br>  "return_policy": null,<br>  "barcode": null,<br>  "additional_charges": null,<br>  "notes": "Thank you for visiting!",<br>  "others": {}<br>}</pre> </td>
</tr><tr><td> <kbd>document.resume</kbd> </td>
<td> <kbd>Resume</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.resume/fake-resume.webp' width='100%' /> </td>
<td> <pre>❌</pre> </td>
</tr><tr><td> <kbd>document.us-drivers-license</kbd> </td>
<td> <kbd>USDriversLicense</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.us-drivers-license/dl3.jpg' width='100%' /> </td>
<td> <pre>{<br>  "issuing_state": "NY",<br>  "license_number": "123456789",<br>  "full_name": "John Doe",<br>  "first_name": "John",<br>  "middle_name": null,<br>  "last_name": "Doe",<br>  "address": {<br>    "street": "123 Main St",<br>    "city": "New York",<br>    "state": "NY",<br>    "zip_code": "10001"<br>  },<br>  "date_of_birth": "1980-05-15",<br>  "gender": "M",<br>  "height": "5'11\"",<br>  "weight": 180.0,<br>  "eye_color": "Blue",<br>  "hair_color": "Brown",<br>  "issue_date": "2022-01-10",<br>  "expiration_date": "2032-01-10",<br>  "license_class": "B",<br>  "donor": true,<br>  "veteran": false<br>}</pre> </td>
</tr><tr><td> <kbd>document.utility-bill</kbd> </td>
<td> <kbd>UtilityBill</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.utility-bill/utility-bill-example.webp' width='100%' /> </td>
<td> <pre>{<br>  "account_number": "123456789",<br>  "date_mailed": "2023-09-15",<br>  "service_for": "John Doe",<br>  "service_address": {<br>    "street": "123 Elm Street",<br>    "city": "Springfield",<br>    "state": "IL",<br>    "zip_code": "62704"<br>  },<br>  "billing_period_start": "2023-08-01",<br>  "billing_period_end": "2023-08-31",<br>  "date_due": "2023-10-15",<br>  "amount_due": 150.75,<br>  "previous_balance": 25.0,<br>  "payment_received": 50.0,<br>  "current_charges": 175.75,<br>  "breakdown_of_charges": [<br>    {<br>      "description": "Electricity Usage",<br>      "amount": 100.75,<br>      "usage": "500 kWh",<br>      "rate": 0.2<br>    },<br>    {<br>      "description": "Service Fee",<br>      "amount": 10.0,<br>      "usage": null,<br>      "rate": null<br>    },<br>    {<br>      "description": "Taxes",<br>      "amount": 65.0,<br>      "usage": null,<br>      "rate": null<br>    }<br>  ],<br>  "payment_options": [<br>    "Online Payment",<br>    "Check by Mail",<br>    "In-Person"<br>  ],<br>  "contact_information": {<br>    "customer_support": "1-800-555-1234",<br>    "billing_inquiries": "1-800-555-5678",<br>    "emergency_services": "911"<br>  }<br>}</pre> </td>
</tr><tr><td> <kbd>document.w2-form</kbd> </td>
<td> <kbd>W2Form</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.w2-form/w2-form.jpg' width='100%' /> </td>
<td> <pre>{<br>  "control_number": "123456789",<br>  "ein": "12-3456789",<br>  "ssn": "987-65-4321",<br>  "employee_name": "John Doe",<br>  "employee_address": {<br>    "street": "123 Main St",<br>    "city": "Anytown",<br>    "state": "NY",<br>    "zip_code": "12345"<br>  },<br>  "employer_name": "Acme Corporation",<br>  "employer_address": {<br>    "street": "456 Elm St",<br>    "city": "Othertown",<br>    "state": "CA",<br>    "zip_code": "67890"<br>  },<br>  "wages_tips_other_compensation": 50000.0,<br>  "federal_income_tax_withheld": 4000.0,<br>  "social_security_wages": 49000.0,<br>  "social_security_tax_withheld": 3036.8,<br>  "medicare_wages_and_tips": 50000.0,<br>  "medicare_tax_withheld": 735.0,<br>  "tax_year": 2022<br>}</pre> </td>
</tr><tr><td> <kbd>aerospace.remote-sensing</kbd> </td>
<td> <kbd>RemoteSensing</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/aerospace.remote-sensing/planet_labs_port.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": "The satellite image depicts a diverse landscape featuring urban development alongside natural features. The central area shows a well-developed residential zone with visible roads and housing structures, indicating a bustling community. Surrounding this urban core are patches of greenery, likely parks or small forested areas, providing a contrast to the built environment. To the east, there is an expansive body of water, possibly a lake or reservoir, bordered by what appears to be a commercial area with several large buildings and parking lots. The western edge of the image reveals agricultural lands, characterized by neatly arranged fields that suggest farming activities. A river meanders through the landscape, connecting various land features and contributing to the region's ecological diversity.",<br>  "objects": [<br>    "residential-area",<br>    "commercial-area",<br>    "park",<br>    "lake",<br>    "farmlands",<br>    "river"<br>  ],<br>  "categories": [<br>    "residential-area",<br>    "commercial-area",<br>    "park",<br>    "lake",<br>    "farmlands",<br>    "river"<br>  ],<br>  "is_visible": true<br>}</pre> </td>
</tr><tr><td> <kbd>healthcare.medical-insurance-card</kbd> </td>
<td> <kbd>MedicalInsuranceCard</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/healthcare.medical-insurance-card/blue_cross_example.jpg' width='100%' /> </td>
<td> <pre>{<br>  "provider_service": {<br>    "provider_service_number": "123456789",<br>    "precertification_number": null<br>  },<br>  "member_information": {<br>    "member_name": "John Doe",<br>    "member_id": "987654321",<br>    "group_number": "ABC123"<br>  },<br>  "pharmacy_plan": {<br>    "rx_bin": "111222333",<br>    "rx_pcn": "444555666",<br>    "rx_grp": null,<br>    "pharmacy_help_desk": "1-800-PHARMACY"<br>  },<br>  "insurance_provider": {<br>    "provider_name": "HealthFirst Insurance Co.",<br>    "network": "PPO Network"<br>  },<br>  "coverage": {<br>    "office_visit": "In-Network: $20 copay",<br>    "specialist_visit": "In-Network: $40 copay",<br>    "urgent_care": "In-Network: $50 visit fee",<br>    "emergency_room": "In-Network: Deductible applies, then 20% coinsurance",<br>    "inpatient_hospital": "In-Network: $1,000 deductible per admission"<br>  }<br>}</pre> </td>
</tr><tr><td> <kbd>retail.ecommerce-product-caption</kbd> </td>
<td> <kbd>RetailEcommerceProductCaption</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/retail.ecommerce-product-caption/Electronics%20-%20Kindle.webp' width='100%' /> </td>
<td> <pre>{<br>  "description": "The product is a sleek, modern e-reader with a high-resolution display and an ergonomic design for comfortable reading. It features adjustable lighting to reduce eye strain in various environments.",<br>  "rating": 85,<br>  "name": "E-Reader Pro",<br>  "brand": "TechRead",<br>  "category": "Electronics / E-readers",<br>  "price": "$199.99",<br>  "color": "Matte Black"<br>}</pre> </td>
</tr><tr><td> <kbd>media.tv-news</kbd> </td>
<td> <kbd>TVNews</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.tv-news/bbc_news_ukraine_screenshot.jpg' width='100%' /> </td>
<td> <pre>{<br>  "description": null,<br>  "chyron": null,<br>  "network": null,<br>  "reporters": null<br>}</pre> </td>
</tr><tr><td> <kbd>media.nfl-game-state</kbd> </td>
<td> <kbd>NFLGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nfl-game-state/packers_cardinals_screenshot.png' width='100%' /> </td>
<td> <pre>{<br>  "description": "The game is currently in progress with Team A leading by a narrow margin.",<br>  "teams": [<br>    {<br>      "name": "Team A",<br>      "score": 21<br>    },<br>    {<br>      "name": "Team B",<br>      "score": 19<br>    }<br>  ],<br>  "status": "in_progress",<br>  "quarter": 3,<br>  "clock_time": "07:32",<br>  "possession_team": "Team A",<br>  "down": "2nd",<br>  "distance": 5,<br>  "yard_line": 45,<br>  "network": "ESPN",<br>  "is_shown": true<br>}</pre> </td>
</tr><tr><td> <kbd>media.nba-game-state</kbd> </td>
<td> <kbd>NBAGameState</kbd> </td>
<td> <img src='https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nba-game-state/heats_spurs.png' width='100%' /> </td>
<td> <pre>{<br>  "description": "The game is currently in progress with Team A leading by a narrow margin.",<br>  "teams": [<br>    {<br>      "name": "Team A",<br>      "score": 102<br>    },<br>    {<br>      "name": "Team B",<br>      "score": 98<br>    }<br>  ],<br>  "status": "in_progress",<br>  "quarter": 3,<br>  "clock_time": "4:32",<br>  "shot_clock": 14,<br>  "network": "ESPN",<br>  "is_shown": true<br>}</pre> </td>
</tr>
</table>
