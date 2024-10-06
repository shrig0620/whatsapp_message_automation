# whatsapp_automatic_message
This Python script automates sending pre-defined WhatsApp messages to multiple contacts using "pywhatkit" package. It calculates the next available time slot and sends messages sequentially to each contact, ensuring a delay between each message. The script runs through WhatsApp Web, allowing seamless automated messaging once you log in via QR code.

#📥 Download My Code

#🔧 Steps to Run the Code:

1.Open your Command Prompt and type
```language
pip install pywhatkit
```

2.After installation, open the Python file whatsapp_automation. Add the WhatsApp numbers you want to send messages to and type the message

```language
contacts = [
    "+919080109689", #Enter numbers with country code
    "+910123456789",
    "+911234567890"
    ]
  
 message = "Hello! This is an automated message from SHRI.G"
```
 Save Your File

3.Run the code by pressing F5 (or executing the script)

4.Your web browser will open with the WhatsApp login page and a QR code

5.Scan the QR code using your phone. Once logged in, the script will automatically start sending messages within 15 seconds! 📱✨

