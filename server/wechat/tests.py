from django.test import TestCase, Client, SimpleTestCase
from django.core.urlresolvers import reverse

from app.models import Parent, Teacher

from .wxapi import wx_dict2xml, wx_xml2dict


class TestWechatPage(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.client.get(reverse('wechat:index'))
        self.assertEqual(response.status_code, 302)

    def test_schools(self):
        response = self.client.get(reverse('wechat:schools'))
        self.assertEqual(response.status_code, 200)

    def test_school_map(self):
        response = self.client.get(reverse('wechat:school-map', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_school_photos(self):
        response = self.client.get(reverse('wechat:school-photos', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_teachers(self):
        response = self.client.get(reverse('wechat:teachers'))
        self.assertEqual(response.status_code, 200)

    def test_order_course_choosing(self):
        pass
        #response = self.client.get(reverse('wechat:order-course-choosing') + '?teacher_id=1')
        #self.assertEqual(response.status_code, 200)
        # TODO: Update

    def test_order_coupon_list(self):
        response = self.client.get(reverse('wechat:order-coupon-list') + '?teacher_id=1')
        self.assertEqual(response.status_code, 200)

    def test_order_evaluate_list(self):
        response = self.client.get(reverse('wechat:order-evaluate-list') + '?teacher_id=1')
        self.assertEqual(response.status_code, 200)

    def test_teacher(self):
        teachers = Teacher.objects.filter(published=True)
        one = list(teachers) and teachers[0]
        if one:
            response = self.client.get(reverse("wechat:teacher") + '?teacher_id=' + str(one.id))
            self.assertEqual(response.status_code, 200)
        else:
            print('TestWechat.test_teacher: no teacher exist!')

    def test_teacher_schools(self):
        data = dict(lat=1, lng=1, tid=1)
        response = self.client.post(reverse('wechat:teacher-schools'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_phone_page(self):
        response = self.client.get(reverse("wechat:phone_page"))
        self.assertEqual(response.status_code, 200)

    def test_add_openid(self):
        response = self.client.get(reverse("wechat:add_openid"))
        self.assertEqual(response.status_code, 200)
        # TODO: check result is True

    def test_check_phone(self):
        response = self.client.get(reverse("wechat:add_openid"))
        self.assertEqual(response.status_code, 200)
        # TODO: check result is True

    def test_pay_notify(self):
        pass  # TODO

    def test_policy(self):
        response = self.client.get(reverse("wechat:policy"))
        self.assertEqual(response.status_code, 200)

    def test_report_sample(self):
        response = self.client.get(reverse("wechat:report-sample"))
        self.assertEqual(response.status_code, 200)

    def test_vip(self):
        response = self.client.get(reverse("wechat:vip"))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(reverse("wechat:register"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("wechat:register") + '?step=success')
        self.assertEqual(response.status_code, 200)


class TestUtils(SimpleTestCase):
    def test_xml_2_dict(self):
        xml_string = '''
            <xml>
               <return_code><![CDATA[SUCCESS]]></return_code>
               <return_msg><![CDATA[OK]]></return_msg>
               <appid><![CDATA[wx2421b1c4370ec43b]]></appid>
               <mch_id><![CDATA[10000100]]></mch_id>
               <nonce_str><![CDATA[IITRi8Iabbblz1Jc]]></nonce_str>
               <sign><![CDATA[7921E432F65EB8ED0CE9755F0E86D72F]]></sign>
               <result_code><![CDATA[SUCCESS]]></result_code>
               <prepay_id><![CDATA[wx201411101639507cbf6ffd8b0779950874]]></prepay_id>
               <trade_type><![CDATA[JSAPI]]></trade_type>
            </xml>
        '''
        xml_dict = wx_xml2dict(xml_string)
        # print(xml_dict)
        self.assertEqual(xml_dict['return_code'], 'SUCCESS')
        self.assertEqual(xml_dict['return_msg'], 'OK')
        self.assertEqual(xml_dict['appid'], 'wx2421b1c4370ec43b')
        self.assertEqual(xml_dict['mch_id'], '10000100')
        self.assertEqual(xml_dict['nonce_str'], 'IITRi8Iabbblz1Jc')
        self.assertEqual(xml_dict['sign'], '7921E432F65EB8ED0CE9755F0E86D72F')
        self.assertEqual(xml_dict['result_code'], 'SUCCESS')
        self.assertEqual(xml_dict['prepay_id'], 'wx201411101639507cbf6ffd8b0779950874')
        self.assertEqual(xml_dict['trade_type'], 'JSAPI')

        xml_string2 = wx_dict2xml(xml_dict)
        # print(xml_string2)

        xml_dict2 = wx_xml2dict(xml_string)
        # print(xml_dict2)
        self.assertEqual(xml_dict2['return_code'], 'SUCCESS')
        self.assertEqual(xml_dict2['return_msg'], 'OK')
        self.assertEqual(xml_dict2['appid'], 'wx2421b1c4370ec43b')
        self.assertEqual(xml_dict2['mch_id'], '10000100')
        self.assertEqual(xml_dict2['nonce_str'], 'IITRi8Iabbblz1Jc')
        self.assertEqual(xml_dict2['sign'], '7921E432F65EB8ED0CE9755F0E86D72F')
        self.assertEqual(xml_dict2['result_code'], 'SUCCESS')
        self.assertEqual(xml_dict2['prepay_id'], 'wx201411101639507cbf6ffd8b0779950874')
        self.assertEqual(xml_dict2['trade_type'], 'JSAPI')
