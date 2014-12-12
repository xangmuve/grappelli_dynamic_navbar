# -*- coding: utf-8 -*-

from django.template import Template, RequestContext
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.test.utils import override_settings
from django.test import TestCase

from grappelli_dynamic_navbar.templatetags.grappelli_dynamic_navbar \
    import applist


class BaseTestCase(TestCase):
    def setUp(self):
        login = 'root'
        email = 'root@local.host'
        password = 'pass123'
        self.user = User.objects.create_superuser(login, email, password)
        self.client = Client()
        self.client.login(username=login, password=password)


class NavBarTestCase(BaseTestCase):
    def test_navbar_default(self):
        factory = RequestFactory()
        request = factory.get(reverse("admin:index"))
        request.user = self.user
        navbar = applist()
        tpl = Template(u"{% load grappelli_dynamic_navbar %}{% grappelli_dynamic_navbar %}")
        self.assertTrue(len(tpl.render(RequestContext(request))) > 0)

    def test_navbar_admin_page(self):
        response = self.client.get(reverse("admin:index"))



