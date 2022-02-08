from ctypes import alignment
import json
from fpdf import FPDF

#PDF Format
pdf = FPDF('P', 'cm', 'A4') 
pdf.add_page()


#Read Informations
Resume_Information= open('InformationResume.json', 'r')
Resume_Maker= Resume_Information.read()
Information_User_Raw= json.loads(Resume_Maker)

#Informations
for Information_User in Information_User_Raw:
    pdf.set_font('times', 'B', 40)
    pdf.cell(18.5,1, f"{Information_User['lastname']} {Information_User['firstname']} {Information_User['middlename']}", align= "C", ln=1)
    pdf.set_font('times', 'I', 12)
    pdf.cell(18.5,2, (Information_User['description']), align= "C", ln=1)
    pdf.set_font('times', "B", 15)
    pdf.cell(5.25,1,"Personal Information", border= 1, ln=1)
    pdf.set_font('helvetica', "", 10)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Address: {Information_User['address']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Email Address: {Information_User['emailadd']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Age: {Information_User['age']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Gender: {Information_User['gender']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Contact Number: {Information_User['contactnumber']}", align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Birthday: {Information_User['birthday']}", align="C",ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Citizenship: {Information_User['citizenship']}", align="C", ln=1)
    pdf.set_font('times', "B", 15)
   
    pdf.cell(1.75,1,"Skills", border=1, ln=1)
    pdf.set_font('helvetica', "", 10)
    for skills in Information_User ['skills']:
        pdf.cell(8.5,1,"", )
        pdf.cell(2,1, (skills), align="C", ln=1)
    pdf.set_font('times', "B", 15)
   
    pdf.cell(3.5,1,"Achievements", border=1, ln=1)
    pdf.set_font('helvetica', "", 10)
    for achievements in Information_User ['achievements']:
        pdf.cell(8.5,1,"", )
        pdf.cell(2,1, (achievements), align="C", ln=1)
    pdf.set_font('times', "B", 15)
    pdf.cell(6,1,"Educational Background", border=1, ln=1)
    pdf.set_font('helvetica', "", 10)
    for educationalbg in Information_User ['educationalbg']:
        pdf.cell(8.5,1,"", )
        pdf.cell(2,1, (educationalbg['School']), align="C", ln=1) 
        pdf.cell(8.5,1,"",)
        pdf.cell(2,1, (educationalbg['AcadYear']), align="C", ln=1) 

#PDF Maker
pdf.output('Murallos_SOLANA.pdf')