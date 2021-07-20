# -*- coding: utf-8 -*-
import frappe
from frappe import format
import unittest

class TestFormatter(unittest.TestCase):
	def test_custom_currency_formatting(self):
		df = frappe._dict({
			'fieldname': 'amount',
			'fieldtype': 'Currency',
			'options': 'currency'
		})

		doc = frappe._dict({
			'amount': 5
		})
		frappe.db.set_default("currency", 'INR')

		# if currency field is not passed then default currency should be used.
		print("doc.currency")
		print(doc.currency)
		print("frappe.db.get_default('currency')")
		print(frappe.db.get_default("currency"))

		self.assertEqual(format(100000, df, doc, format="#,###.##"), '₹ 100,000.00')

		doc.currency = 'USD'
		self.assertEqual(format(100000, df, doc, format="#,###.##"), "$ 100,000.00")

		frappe.db.set_default("currency", None)
