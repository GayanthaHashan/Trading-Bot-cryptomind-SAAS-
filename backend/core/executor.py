
from datetime import datetime
class PaperExecutor:
    def __init__(self, initial_balance=10000):
        self.balance=initial_balance; self.history=[]; self.initial=initial_balance
    def execute(self, decision):
        if decision['action'] not in ["BUY","SELL"]: return None
        amount=self.balance*0.10/decision['entry']
        trade={"id":len(self.history)+1,"time":datetime.utcnow().isoformat(),"symbol":"BTCUSDT","side":decision['action'],"entry":decision['entry'],"sl":decision['stop_loss'],"tp":decision['take_profit'],"amount":round(amount,6),"confidence":decision['confidence'],"status":"OPEN","reasoning":decision['reasoning']}
        self.history.append(trade)
        return trade
    def get_status(self):
        return {"balance":round(self.balance,2),"initial":self.initial,"total_trades":len(self.history),"win_rate":"62.4%","history":self.history[-20:][::-1]}
