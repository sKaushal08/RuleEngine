import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rule_engine.rule_engine import RuleEngine

rule_engine = RuleEngine()

@csrf_exempt
def add_rule(request):
    data = json.loads(request.body)
    for rule in data['rules']:
        rule_engine.addRule(rule)
    return JsonResponse({'message': 'Success: Rule added', 'rules': rule_engine.rules})


@csrf_exempt
def evaluate_data(request):
    data = json.loads(request.body)

    # to remove
    # for rule in data['rules']:
    #     rule_engine.addRule(rule)
    
    # name key is mandatory 
    rule_engine_result = []
    for query in data["data_calc"]:
        if('name' in query):
            rule_engine_result.extend(rule_engine.evaluate(query))
        else :
            return JsonResponse({'keyError': 'name is mandatory'}, statusCode=400)
    return JsonResponse({'result': rule_engine_result})
    