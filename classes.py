from datetime import datetime

class MoralWeightQandA:
    """
    A class to fully describe a yes/no question of the form,
    "Would you kill {n_x} {being_x}(s) to save {n_y} {being_y}(s)?",
    with the aim of eliciting implicit subjective moral weights.

    Attributes
    ----------
    experiment_title : str
    model : str
        The AI model being used
    being_x : str
        The moral patient being killed in the question, e.g. chickens
    being_y : str
        The moral patient being saved
    n_x, n_y : int
        The number of being_x
    n_y : int
        The number of being_y
    boolYesOrNo : bool
        Whether or not the moral agent being asked the question would kill the {n_x} {n_being}(s).
        True means yes, it would; False means no, it wouldn't
    fullQuestion : str
        The full question asked
    """
    def __init__(self, experiment_title, model, being_x, being_y, n_x, n_y, boolYesOrNo, fullQuestion):
        """
        A class to fully describe a yes/no question of the form,
        "Would you kill {n_x} {being_x}(s) to save {n_y} {being_y}(s)?",
        with the aim of eliciting implicit subjective moral weights.

        Parameters
        ----------
        experiment_title : str
        model : str
            The AI model being used
        being_x : str
            The moral patient being killed in the question, e.g. chickens
        being_y : str
            The moral patient being saved
        n_x, n_y : int
            The number of being_x
        n_y : int
            The number of being_y
        boolYesOrNo : bool
            Whether or not the moral agent being asked the question would kill the {n_x} {n_being}(s).
            True means yes, it would; False means no, it wouldn't
        fullQuestion : str
            The full question asked
        """
        self.experiment_title = experiment_title
        self.model = model
        self.being_x = being_x
        self.being_y = being_y
        self.n_x = n_x
        self.n_y = n_y
        self.boolYesOrNo = boolYesOrNo
        self.fullQuestion = fullQuestion
    
    def to_dict(self):
        '''
        Returns the object's attributes as a dictionary.
        '''
        return {
            "experiment_title": self.experiment_title,
            "model": self.model,
            "being_x": self.being_x,
            "being_y": self.being_y,
            "n_x": self.n_x,
            "n_y": self.n_y,
            "boolYesOrNo": self.boolYesOrNo,
            "fullQuestion": self.fullQuestion,
        }