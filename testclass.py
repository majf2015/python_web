class TestClass:
    def __init__(self, method):
        self.method = method
        self.case = []
        self.result = []

    def add(self, case, result):
        self.case.append(case)
        self.result.append(result)

    def adds(self, cases, results):
        for i in range(len(cases)):
            self.add(cases[i], results[i])

    def test_run(self):
        for i in range(len(self.case)):
            fact_result = self.method(self.case[i])
            if fact_result == self.result[i]:
                print "successful", i

            else:
                print "error", i
                print fact_result