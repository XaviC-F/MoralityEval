from datetime import datetime

class MoralWeightQuestion:
    """
    A class to fully describe a yes/no question of the form,
    "Would you kill {n_x} {being_x}(s) to save {n_y} {being_y}(s)?",
    with the aim of eliciting implicit subjective moral weights.

    Attributes
    ----------
    experiment_number : int
        The ordinal experiment number
    experiment_description : str
    being_x, being_y : str
        The two moral patients in the question, e.g. chickens and humans
    n_x, n_y : int
        The number of moral patients for being_x and being_y respectively
    boolYesOrNo : bool
        Whether or not the moral agent being asked the question would kill the {n_x} {n_being}(s).
        True means yes, it would; False means no, it wouldn't
    fullQuestion, fullAnswer : str
        The full question and answers given, including all thinking
    """
    def __init__(self,experiment_number, experiment_description, being_x, being_y, n_x, n_y, boolyesOrNo, fullQuestion, fullAnswer):
        """
        A class to fully describe a yes/no question of the form,
        "Would you kill {n_x} {being_x}(s) to save {n_y} {being_y}(s)?",
        with the aim of eliciting implicit subjective moral weights.

        Parameters
        ----------
        experiment_number : int
            The ordinal experiment number
        experiment_description : str
        being_x, being_y : str
            The two moral patients in the question, e.g. chickens and humans
        n_x, n_y : int
            The number of moral patients for being_x and being_y respectively
        boolYesOrNo : bool
            Whether or not the moral agent being asked the question would kill the {n_x} {n_being}(s).
            True means yes, it would; False means no, it wouldn't
        fullQuestion, fullAnswer : str
            The full question and answers given, including all thinking
        """
        self.timestamp = datetime.now().isoformat()
        self.experiment_number = experiment_number
        self.experiment_description = experiment_description
        self.being_x = being_x
        self.being_y = being_y
        self.n_x = n_x
        self.n_y = n_y
        self.boolyesOrNo = boolyesOrNo
        self.fullQuestion = fullQuestion
        self.fullAnswer = fullAnswer
    
    def to_dict(self):
        '''
        Returns the object's attributes as a dictionary.

        Returns
        ----------
        experiment_number : int
            The ordinal experiment number
        experiment_description : str
        being_x, being_y : str
            The two moral patients in the question, e.g. chickens and humans
        n_x, n_y : int
            The number of moral patients for being_x and being_y respectively
        boolYesOrNo : bool
            Whether or not the moral agent being asked the question would kill the {n_x} {n_being}(s).
            True means yes, it would; False means no, it wouldn't
        fullQuestion, fullAnswer : str
            The full question and answers given, including all thinking
        '''
        return {
            "timestamp": self.timestamp,
            "experiment_number": self.experiment_number,
            "experiment_description": self.experiment_description,
            "being_x": self.being_x,
            "being_y": self.being_y,
            "n_x": self.n_x,
            "n_y": self.n_y,
            "boolyesOrNo": self.boolyesOrNo,
            "fullQuestion": self.fullQuestion,
            "fullAnswer": self.fullAnswer,
        }