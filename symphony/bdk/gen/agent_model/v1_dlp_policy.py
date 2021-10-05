"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.13.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
from typing import List

from symphony.bdk.gen.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

from symphony.bdk.gen.agent_model.v1_dlp_dictionary_ref import V1DLPDictionaryRef
globals()['V1DLPDictionaryRef'] = V1DLPDictionaryRef


class V1DLPPolicy(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a agent_model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'content_types': ([str],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'scopes': ([str],),  # noqa: E501
            'type': (str,),  # noqa: E501
            'active': (bool, none_type),  # noqa: E501
            'creation_date': (int, none_type),  # noqa: E501
            'creator_id': (str, none_type),  # noqa: E501
            'dictionary_refs': ([V1DLPDictionaryRef], none_type),  # noqa: E501
            'last_disabled_date': (int, none_type),  # noqa: E501
            'last_updated_date': (int, none_type),  # noqa: E501
            'policy_id': (str, none_type),  # noqa: E501
            'version': (str, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'content_types': 'contentTypes',  # noqa: E501
        'name': 'name',  # noqa: E501
        'scopes': 'scopes',  # noqa: E501
        'type': 'type',  # noqa: E501
        'active': 'active',  # noqa: E501
        'creation_date': 'creationDate',  # noqa: E501
        'creator_id': 'creatorId',  # noqa: E501
        'dictionary_refs': 'dictionaryRefs',  # noqa: E501
        'last_disabled_date': 'lastDisabledDate',  # noqa: E501
        'last_updated_date': 'lastUpdatedDate',  # noqa: E501
        'policy_id': 'policyId',  # noqa: E501
        'version': 'version',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, content_types, name, scopes, type, *args, **kwargs):  # noqa: E501
        """V1DLPPolicy - a agent_model defined in OpenAPI

        Args:
            content_types ([str]): The list of content types that policy should apply to. Cannot be empty. Policy content types could be either of \"Messages\", \"RoomMeta\", \"SignalMeta\". Default is set to [\"Messages\"] if not specified. 
            name (str): Unique name of a policy, max 30 characters. Cannot be empty. All the leading and trailing blank spaces are trimmed.
            scopes ([str]): List of communication scopes. Possible values are \"Internal\" (for Internal conversations) or \"External\" (for External conversations). You can apply both scopes if you set it to [\"Internal\", \"External\"]. 
            type (str): Type of policy. Possible values \"Block\" or \"Warn\".

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the agent_model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active (bool): Indicate whether the policy is active or not. [optional]  # noqa: E501
            creation_date (int): Creation time of the policy in milliseconds elapsed as of epoch time. . [optional]  # noqa: E501
            creator_id (str): Numeric userId of the creator. [optional]  # noqa: E501
            dictionary_refs ([V1DLPDictionaryRef]): List of dictionaries.. [optional]  # noqa: E501
            last_disabled_date (int): Recent disable time of the policy in milliseconds elapsed as of epoch time. . [optional]  # noqa: E501
            last_updated_date (int): Recent update time of the policy in milliseconds elapsed as of epoch time.. [optional]  # noqa: E501
            policy_id (str): Policy Id. [optional]  # noqa: E501
            version (str): The version of a dictionary, in format \"major.minor\". Initial value will set by backend as \"1.0\" when created. Whenever the dictionary version needs to be changed, the minor version by 1 unless minor == 999, then the major version is increased by 1 until it reaches 999. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.content_types: List[str] = content_types
        self.name: str = name
        self.scopes: List[str] = scopes
        self.type: str = type
        self.active: bool = None
        self.creation_date: int = None
        self.creator_id: str = None
        self.dictionary_refs: List[V1DLPDictionaryRef] = None
        self.last_disabled_date: int = None
        self.last_updated_date: int = None
        self.policy_id: str = None
        self.version: str = None
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
