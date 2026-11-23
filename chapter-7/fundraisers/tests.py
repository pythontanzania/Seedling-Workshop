from django.contrib.auth.models import User
from django.test import TestCase

from .models import Fundraiser, Payment, Pledge


class FlowTest(TestCase):
    def test_flow(self):
        e = Fundraiser.objects.create(name="Desks for Kilele Primary", target=500000)
        r = self.client.get("/")
        self.assertContains(r, "Desks for Kilele Primary")
        self.assertContains(r, "(0%)")
        r = self.client.post(f"/fundraiser/{e.id}/pledge/", {"name": "Juma", "phone": "071234", "amount": 500})
        self.assertContains(r, "Use 10 digits")
        self.assertContains(r, "smallest pledge")
        r = self.client.post(f"/fundraiser/{e.id}/pledge/", {"name": "Juma", "phone": "0712345678", "amount": 100000})
        self.assertRedirects(r, f"/fundraiser/{e.id}/")
        p = Pledge.objects.get()
        r = self.client.get(f"/fundraiser/{e.id}/")
        self.assertContains(r, "Lipa")
        self.assertNotContains(r, "0712345678")
        r = self.client.get(f"/pledge/{p.id}/lipa/")
        self.assertContains(r, "TZS 100,000")
        r = self.client.post(f"/pledge/{p.id}/callback/")
        self.assertContains(r, "Payment received")
        self.assertEqual(Payment.objects.count(), 1)
        r = self.client.post(f"/pledge/{p.id}/callback/")
        self.assertEqual(Payment.objects.count(), 1)
        r = self.client.get(f"/fundraiser/{e.id}/")
        self.assertContains(r, "Paid in full")
        self.assertContains(r, "(20%)")
        r = self.client.get("/manage/")
        self.assertRedirects(r, "/accounts/login/?next=/manage/")
        User.objects.create_user("mama", password="pass12345!")
        r = self.client.post("/accounts/login/", {"username": "mama", "password": "pass12345!"})
        self.assertRedirects(r, "/manage/")
        r = self.client.get("/manage/")
        self.assertContains(r, "0712345678")
        r = self.client.post("/manage/new/", {"name": "School desks", "description": "", "target": 2000000})
        self.assertEqual(Fundraiser.objects.count(), 2)
        r = self.client.post("/accounts/logout/")
        self.assertRedirects(r, "/")
