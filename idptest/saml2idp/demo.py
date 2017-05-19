import base
import exceptions
import xml_render

class Processor(base.Processor):
    """
    Demo Response Handler Processor for testing against django-saml2-sp.
    """
    def _format_assertion(self):
        # NOTE: This uses the SalesForce assertion for the demo.
        self._assertion_xml = xml_render.get_assertion_salesforce_xml(self._assertion_params, signed=True)


class AttributeProcessor(base.Processor):
    """
    Demo Response Handler Processor for testing against django-saml2-sp;
    Adds SAML attributes to the assertion.
    """
    def _format_assertion(self):
        # NOTE: This uses the SalesForce assertion for the demo.
        """
        SAML_ATTRIBUTE_MAPPING = {
            'uid': ('username', ),
            'mail': ('email', ),
            'cn': ('first_name', ),
            'sn': ('last_name', ),
        }
        """

        self._assertion_params['ATTRIBUTES'] = {
            'uid': 'broekej',
            'mail': 'johan@fullscreen.nl',
            'cn': 'Johan',
            'sn': 'ten Broeke',
        }

        self._assertion_xml = xml_render.get_assertion_salesforce_xml(self._assertion_params, signed=True)
