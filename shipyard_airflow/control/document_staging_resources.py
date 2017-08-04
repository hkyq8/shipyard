# Copyright 2017 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import falcon
import json
import requests

from .base import BaseResource

ALLOWED_TYPES = ()
def validate_file_type(req,resp,resource,params):
    if req.content_type not in ALLOWED_TYPES:
        msg = 'File type not supported. Must be YAML'
        raise falcon.HTTPBadRequest('Bad Request', msg)


class DocumentResource(BaseResource):
    authorized_roles = ['user']

    # @falcon.before(validate_file_type)
    def on_post(self,req, resp):
        document_data = req.stream.read(req.content_length or 0)

    

    def on_get(self,req, resp):
        last_deployed =  req.params.get('lastDeployed').lower()
        if last_deployed == 'true':
            # TODO return the Documents for the currently deployed version
            pass
        else:
            # TODO return the documents for the most recently staged version
            pass


    def on_delete(self,req,resp):
        # TODO updates configdocs to be the lastdeployed versions in deckhand
        










