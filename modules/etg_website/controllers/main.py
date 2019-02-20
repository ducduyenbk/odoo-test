from odoo import http
from odoo.http import request
import requests


class WebsiteRegister(http.Controller):

    @http.route('/register', type='http', auth='public', website=True)
    def register(self):
        products = request.env['product.template'].search([])
        return http.request.render('etg_website.register', {'products': products})

    @http.route('/register/submit', type='http', methods=['POST'], website=True, auth="public")
    def register_submit(self, **kw):

        # kiem tra short_name

        # tao crm.lead
        lead = request.env['crm.lead']
        lead_data = {
            'name': kw['contact_name'] + " are using trial of " + kw['product'],
            'email_from': kw['email'],
            'phone': kw['mobile'],
            'partner_name': kw['partner_name'],
            'short_name': kw['short_name'],
            'contact_name': kw['contact_name'],
        }
        try:
            lead.sudo().create(lead_data)
        except:
            return http.request.render('etg_website.error')

        # goi api
        url = "http://35.194.160.6:9000/api/register"
        api_data = {
            "name": kw['contact_name'],
            "phone": kw['mobile'],
            "email": kw['email'],
            "company": kw['partner_name'],
            "product": kw['product'],
            "short_name": kw['short_name'],
            "password": kw['password']
        }
        try:
            requests.post(url, data=api_data)
        except:
            return http.request.render('etg_website.error')

        return http.request.render('etg_website.thanks')
