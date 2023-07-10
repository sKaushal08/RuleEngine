class RuleEngine:
    def __init__(self):
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule)

    
    def evaluate(self, query):
        result = []
        for rule in self.rules:
            conditions = rule['conditions']
            if all(self.evaluateCondition(condition, query) for condition in conditions):      
                result.append({'name': query['name'], 'value': rule['actions']})
            
        return result

    def evaluateCondition(self, condition, data):
        variable = condition['var_name']
        operator = condition['operator']
        edge_value = condition['edge_value']

        if operator == '>':
            return data[variable] > edge_value
        elif operator == '<':
            return data[variable] < edge_value
        elif operator == '>=':
            return data[variable] >= edge_value
        elif operator == '<=':
            return data[variable] <= edge_value
        elif operator == '==':
            return data[variable] == edge_value
        elif operator == 'startsWith':
            return data[variable].startswith(edge_value)
        elif operator == 'endsWith':
            return data[variable].endswith(edge_value)
        elif operator == 'length':
            return len(data[variable]) == edge_value
        else:
            return False
                