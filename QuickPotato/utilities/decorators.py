from QuickPotato.harness.reporting import BoundariesTestEvidence
from QuickPotato.utilities.exceptions import NeedsKeyWordArguments
from functools import wraps


def save_boundary_evidence(fnc):
    """

    Parameters
    ----------
    fnc

    Returns
    -------

    """

    @wraps(fnc)
    def encapsulated_method(*args, **kwargs):
        """

        Parameters
        ----------
        args
        kwargs

        Returns
        -------

        """
        if len(args) > 1:
            raise NeedsKeyWordArguments()

        evidence = BoundariesTestEvidence()
        evidence.test_id = kwargs["test_id"]
        evidence.test_case_name = kwargs["test_case_name"]
        evidence.verification_name = kwargs["validation_name"]
        evidence.value = float(kwargs["value"])
        evidence.boundary = float(kwargs["boundary"])

        # Scrub unused meta data
        del kwargs["test_id"]
        del kwargs["test_case_name"]
        del kwargs["validation_name"]

        evidence.status = fnc(*args, **kwargs)
        evidence.save()

        return evidence.status

    return encapsulated_method
