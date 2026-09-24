
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade:
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor):
      self.payment_processor=payment_processor
      self.beingsubscribed= False
   
      

    def subscribe(self, monthly_fee: float) -> str:
      ticket=self.payment_processor.pay(monthly_fee)
      self.beingsubscribed=True
      return ticket
    
      

    def watch(self, video: Video) -> str:
      if not self.beingsubscribed:
          raise PermissionError("subscription required")
      # TODO: if not subscribed, raise PermissionError("subscription required").
      # Otherwise delegate to `video.play()` and return its result.
      return video.play()
