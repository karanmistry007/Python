try:
    print("Success")
    # import frappe
    # from frappe.utils import now_datetime

    # @frappe.whitelist()
    # def sales_invoice_create(
    #     customer,
    #     request_for_service="",
    #     request_for_parts="",
    #     supplier="",
    #     due_date="",
    #     items="",
    # ):

    #     check_invoice = None
    #     # GET THE LIST OF THE DUPLICATE DATA
    #     # check_invoice = frappe.db.get_list(
    #     #     "Sales Invoice",
    #     #     filters={
    #     #         "status": "Unpaid",
    #     #         "customer": customer,
    #     #         "custom_request_for_service": request_for_service,
    #     #     },
    #     #     fields=["name"],
    #     # )

    #     # IF THERE IS A DUPLICATE REQUEST EXISTS
    #     if check_invoice:

    #         return "The Unpaid Sales Invoice Is Already Available With The Same Request"

    #     # IF THERE IS NO DUPLICATE DATA
    #     else:
    #         # CREATE A NEW SALES INVOICE
    #         new_invoice = frappe.new_doc("Sales Invoice")
    #         new_invoice.customer = customer
    #         new_invoice.due_date = due_date
    #         new_invoice.custom_request_for_service = request_for_service
    #         new_invoice.custom_request_for_parts = request_for_parts
    #         new_invoice.custom_supplier = supplier
    #         new_invoice.company_gstin = ""

    #         if request_for_parts:
    #             doc_request_for_parts = frappe.get_doc(
    #                 "Request For Parts", request_for_parts
    #             )
    #             for row in doc_request_for_parts.parts:

    #                 new_invoice.append(
    #                     "items",
    #                     {"item_code": row.item_code, "qty": row.qty, "rate": row.rate},
    #                 )

    #         elif items:
    #             # CONVERT JSON DATA TO PYTHON LIST
    #             items = frappe.parse_json(items)

    #             # FOR ITEMS IN LIST (FOR ROW IN TABLE)
    #             for item in items:

    #                 # APPEND ROWS INSIDE THE TABLE
    #                 new_invoice.append("items", item)

    #         try:
    #             new_invoice.insert()
    #             new_invoice.submit()

    #         except Exception as e:
    #             frappe.db.rollback()
    #             return f"{e}"

    #         frappe.db.commit()
    #         return "The Request Has Been Created Successfully"

except Exception as e:
    print(f"Bhai Error AAi")

finally:
    print("Finnalyy")
