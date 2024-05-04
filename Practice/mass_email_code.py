import os
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render


def send_mass_email_view(request):
    if request.method == "POST":
        subject = "Your Subject Here"  # Replace with your email subject
        message = (
            "Dear Team,\n\n" "Your message here.\n\n" "Thank you!\n"
        )  # Replace with your email message
        from_email = (
            settings.EMAIL_HOST_USER
        )  # Sender's email address (configured in settings)

        # Get a list of recipients from a CSV file, database, or any other source.
        recipients = [
            "ksmistry007@gmail.com",
            "hetalmistry022@gmail.com",
            "Karanmistry2501@gmail.com",
            "vivekmanish1023@gmail.com",
            "vivekpriya4509@gmail.com",
            "vivekpriya@karmamepf.com",
        ]

        for recipient in recipients:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=[recipient],
            )
            email.send()

        return render(request, "product/success.html")

    return render(request, "product/mass_email_form.html")
