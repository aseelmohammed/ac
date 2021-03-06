# -*- coding: utf-8 -*-
# Copyright (c) 2021, Aseel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.contacts.address_and_contact import load_address_and_contact, delete_contact_and_address
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class AdministrativeCommunicationParty(NestedSet):
	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)
