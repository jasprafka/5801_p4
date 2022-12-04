class Problem():
    def __init__(self,prob_type) -> None:
        self.prob_type = prob_type 
        self.line_tuples = []
    
    def __repr__(self)->str:
        return f"Problem Type: {self.prob_type}\nLines:" + ','.join(map(str, self.line_tuples))
        