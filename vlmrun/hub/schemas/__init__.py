from vlmrun.hub.registry import Registry


def import_all():
    from vlmrun.hub.schemas.aerospace.remote_sensing import RemoteSensing
    from vlmrun.hub.schemas.document.invoice import Invoice
    from vlmrun.hub.schemas.contrib.banking.document_verification import DocumentVerification
    from vlmrun.hub.schemas.healthcare.medical_insurance_card import MedicalInsuranceCard

    Registry.register("aerospace.remote-sensing", RemoteSensing)
    Registry.register("document.invoice", Invoice)
    Registry.register("healthcare.medical-insurance-card", MedicalInsuranceCard)
    Registry.register("contrib.banking.document-verification", DocumentVerification)
