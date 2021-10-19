from urllib import error as error
import json
import requests
from ansible.module_utils.basic import AnsibleModule

def __api_call(module):
        base_url=module.params.get('url')
        data=module.params.get('data')
        access_token=module.params.get('access_token')
        url = str(base_url)
        header = { "Authorization": 'Bearer {0}'.format(access_token),
                                "Content-Type": 'application/json'}      
#       epoch = module.params.get("epoch")
        request = requests.put(url, headers=header, data=json.dumps(data))
        try:   
            response = { "json": str(request.content) } 
            module.exit_json(changed=True,json=response)
        except Exception as e:
                        module.fail_json(
                            msg="Error, token is invalid or error in request "
                        )
    
def main():
    
    arg = { 
             "url": {"type": "str"},
             "data": {"type": "list"},
             "access_token": {"type": "str"},
            }
    fields = dict(
        url=dict(required=True, type='str'),
        data=dict(required=True, type='dict'),
        access_token=dict(required=True, type='str'),
    )
    
    required_together = [["url", "access_token"]]

    module = AnsibleModule(
        argument_spec=fields,
        required_together=required_together,
        supports_check_mode=True
    )
    (changed, json) = __api_call(module)
    module.exit_json(changed=changed, json=json)

if __name__ == '__main__':
    main()

