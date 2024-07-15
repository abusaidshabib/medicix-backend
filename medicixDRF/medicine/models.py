from django.db import models
from branch.models import BaseModel
from django.utils.translation import gettext as _

from branch.models import Branch

class Medicine(BaseModel):
    brand = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(max_length=255)
    generic = models.CharField(max_length=150)
    strength = models.CharField(max_length=150)
    subcategory = models.ForeignKey("content.Subcategory", on_delete=models.CASCADE, related_name='medicines')
    price = models.FloatField()

    MEDICINE_CATEGORY = [
        ("TAB", "Tablet"),
        ("CAP", "Capsule"),
        ("DISP", "Dispersible Tablet"),
        ("PS", "Powder For Suspension"),
        ("SYR", "Syrup"),
        ("SUSP", "Suspension"),
        ("PD", "Paediatric Drops"),
        ("LOT", "Lotion"),
        ("OIN", "Ointment"),
        ("OS", "Oral Saline"),
        ("CRM", "Cream"),
        ("GEL", "Gel"),
        ("SUPP", "Suppository"),
        ("SOL", "Solution"),
        ("INJ", "Injection"),
        ("ID", "IV Injection"),
        ("IIM", "IV/IM Injection"),
        ("ED", "Eye Drops"),
        ("TS", "Topical Solution"),
        ("BOL", "Bolus"),
        ("PDR", "Powder"),
        ("WSP", "Water Soluble Powder"),
        ("ORS", "Oral Solution"),
        ("OPD", "Oral Powder"),
        ("EED", "Eye and Ear Drops"),
        ("IMI", "IM Injection"),
        ("EEN", "Eye, Ear & Nasal Drops"),
        ("VAG", "Vaginal Tablet"),
        ("HR", "Hand Rub"),
        ("OG", "Oral Gel"),
        ("GMW", "Gargle & Mouth Wash"),
        ("XRT", "Xr Tablet"),
        ("SRT", "Sr Tablet"),
        ("RM", "Raw Materials"),
        ("PEL", "Pellets"),
        ("EO", "Eye Ointment"),
        ("MOW", "Mouth Wash"),
        ("SRC", "Sr Capsule"),
        ("AI", "Aerosol Inhalation"),
        ("INH", "Inhaler"),
        ("IS", "Inhalation Solution"),
        ("IVI", "IV Infusion"),
        ("ORT", "Ors Tablet"),
        ("ODT", "Orodispersible Tablet"),
        ("NS", "Nebuliser Solution"),
        ("OP", "Oral Paste"),
        ("NAS", "Nasal Spray"),
        ("SPR", "Spray"),
        ("DRT", "Dr Tablet"),
        ("COZ", "Cozycap"),
        ("INA", "Inhalation Aerosol"),
        ("INC", "Inhalation Capsule"),
        ("NAD", "Nasal Drops"),
        ("CHT", "Chewable Tablet"),
        ("CRT", "Cr Tablet"),
        ("ERT", "Er Tablet"),
        ("SL", "Scalp Lotion"),
        ("ORD", "Oral Drops"),
        ("GFS", "Granules For Suspension"),
        ("ORSU", "Oral Suspension"),
        ("MUP", "Mups Tablet"),
        ("ILL", "Inhalation Liquid"),
        ("LQD", "Liquid"),
        ("EMU", "Emulsion"),
        ("OLQ", "Oral Liquid"),
        ("PFS", "Pellets For Suspension"),
        ("SCH", "Sachet"),
        ("ELX", "Elixir"),
        ("LIN", "Linctus"),
        ("MDT", "Mouth Dissolving Tablet"),
        ("SGC", "Soft Gelatin Capsule"),
        ("SPD", "Sached Powder"),
        ("EDR", "Ear Drop"),
        ("END", "Eye & Nasal Drops"),
        ("SHA", "Shampoo"),
        ("OPE", "Ophthalmic Emulsion"),
        ("EG", "Eye Gel"),
        ("SFI", "Solution For Injection"),
        ("NSU", "Nebuliser Suspension"),
        ("SFI", "Solution For Infusion"),
        ("MDI", "Metered Dose Inhaler"),
        ("DPI", "Dry Powder Inhaler"),
        ("ODT", "Odt Tablet"),
        ("IRS", "Irrigation Solution"),
        ("ROO", "Rectal Ointment"),
        ("RES", "Resperitory Solution"),
        ("VGC", "Vaginal Cream"),
        ("RES", "Respirator Suspension"),
        ("OSF", "Oral Soluble Film"),
        ("EMU", "Emulgel"),
        ("OEM", "Oral Emulsion"),
        ("RDT", "Rapid Tablet"),
        ("ETT", "Effervescent Tablet"),
        ("CMB", "Combipack"),
        ("HFI", "Hfa Inhaler"),
        ("POS", "Pour On (Solution)"),
        ("PPD", "Powder for Pedriatric Drop"),
        ("EGS", "Effervescent Granules"),
        ("ERC", "Extended Release Capsule"),
        ("MWA", "Mouth Wash Antiseptic"),
        ("SYR", "Syringe"),
        ("DS", "Dialysis Solution"),
        ("PRL", "Per Rectal"),
        ("VGC", "Vaginal Gel"),
        ("PRT", "Pr Tablet"),
        ("DRG", "Dr Granules For Suspension"),
        ("ERC", "Er Capsule"),
        ("CRC", "Cr Capsule"),
        ("GS", "Gas"),
        ("TIN", "Tincture"),
        ("SCR", "Scrub"),
        ("BB", "Blood bag"),
        ("PVB", "Pvc Bag"),
        ("PS", "Powder for Solution"),
        ("ERS", "Ear Spray"),
        ("BTS", "Blood Tubing Set"),
        ("POS", "Powder For Oral Solution"),
        ("OGS", "Oral Granules"),
        ("NFS", "Needle for Syringe"),
        ("BFL", "Butterfly"),
        ("ECS", "Eye Cleanser Solution"),
        ("EEO", "Eye and Ear Ointment"),
        ("DRC", "Delayed Release Capsule"),
        ("WFI", "Water For Injection"),
        ("CG", "Cervical Gel"),
        ("VPS", "Vaginal Pessary"),
        ("GU", "Gum"),
        ("ODG", "Oral Dental Gel"),
        ("TOS", "Topical Suspension"),
        ("MDT", "Md Tablet"),
        ("IMP", "Implant"),
        ("VSS", "Viscoelastic Solution"),
        ("DRO", "Drops"),
        ("VSP", "Vaginal Suppository"),
        ("ESO", "Eye Solution"),
        ("SCO", "Scalp Ointment"),
        ("SPC", "Sprinkle Capsule"),
        ("MRC", "M R Capsule"),
        ("MRT", "M R Tablet"),
        ("RCA", "Root Canal Agent"),
        ("CIR", "Canal Irrigation"),
        ("SFR", "Solution Fo Root Cannel"),
        ("RPA", "Repacking")
    ]

    MEDICINE_FOR = [
        ("H","Human"),
        ("V","Veterinary"),
        ("R","R"),
    ]
    medicine_type = models.CharField(max_length=50, choices=MEDICINE_CATEGORY)
    use_for = models.CharField(max_length=50, choices=MEDICINE_FOR)
    dar = models.CharField(max_length=200)

    def __str__(self):
        return self.generic

class Inventory(BaseModel):
    medicine = models.ForeignKey(Medicine, verbose_name=_("Medicine"), on_delete=models.CASCADE, related_name='inventories')
    branch = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.CASCADE)
    quantity = models.IntegerField()
    soled = models.IntegerField(blank=True, null=True)
    expire_date = models.DateField()

    class Meta:
        unique_together = ["medicine", "branch"]

    def __str__(self):
        return f"{self.medicine} at {self.branch}"

    def clean(self):
        if self.soled > self.quantity:
            raise ValidationError(_("The sold quantity cannot exceed the available quantity."))