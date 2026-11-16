# pickup_queue.py
# Author: Luke Mikhail


class PickupQueue:
    """Pickup requests waiting for staff approval."""

    def __init__(self):
        """Start with an empty list of pickup requests."""
        self.requests = []

    def request_pickup(self, item, location):
        """Submit a pickup request for staff approval.

        Args:
            item: The product the customer wants.
            location: The store location for pickup.
        """
        number = len(self.requests) + 1
        request = {
            "number": number,
            "item": item,
            "location": location,
            "status": "waiting",
        }
        self.requests.append(request)
        return f"Pickup request {number} was sent to staff for approval."

    def waiting(self):
        """Return pickup requests that are waiting for approval."""
        return [request for request in self.requests if request["status"] == "waiting"]

    def approve(self, number):
        """Approve a pickup request once."""
        for request in self.requests:
            if request["number"] == number:
                if request["status"] != "waiting":
                    return f"Request {number} is already {request['status']}."
                request["status"] = "approved"
                return f"Pickup request {number} approved."
        return f"There is no request {number}."

    def reject(self, number):
        """Reject a pickup request once."""
        for request in self.requests:
            if request["number"] == number:
                if request["status"] != "waiting":
                    return f"Request {number} is already {request['status']}."
                request["status"] = "rejected"
                return f"Pickup request {number} rejected."
        return f"There is no request {number}."
