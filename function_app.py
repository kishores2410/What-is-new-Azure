"""
This is a Python Azure Function that is triggered every 12 hours.
It checks if the timer is past due and if so, it logs a message and calls the main function from the feed_processor module.
"""

import logging
import azure.functions as func

from feed_processor import main

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
app = func.FunctionApp()

@app.schedule(schedule="0 */12 * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    """
    This function is triggered by a timer. If the timer is past due, it logs a message.
    Then it calls the main function and logs another message indicating that it has been executed.

    Args:
        myTimer (func.TimerRequest): The timer request object.

    Returns:
        None
    """
    if myTimer.past_due:
        logging.info('The timer is past due!')
    main()
    logging.info('Python timer trigger function executed.')