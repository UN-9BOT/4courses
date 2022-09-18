from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory='templates')


class Wallet:
    __slots__ = ['address', 'balance', 'time_create', 'total_transfers']
    __total_wallets = 0

    def __init__(self):
        self.__and_one()
        self.time_create: datetime = datetime.now()
        self.address = f'0x{Wallet.__total_wallets}'
        self.balance: int = 0
        self.total_transfers = 0

    @classmethod
    def __and_one(cls):
        """Добавление кошелька в total_wallets при создании"""
        cls.__total_wallets += 1

    @classmethod
    def __how_many_wallets(cls):
        """Вывод кол-ва кошельков"""
        return cls.__total_wallets

    def info(self):
        return f'Address wallet: {self.address}, balance = {self.balance}, дата создания = {self.time_create}'


all_wallets = []
for _ in range(10):
    all_wallets.append(Wallet())


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'all_wallets': all_wallets})


@app.get("/wallet/{address}", response_class=HTMLResponse)
def wallet(address: str, request: Request):
    target_address = None
    for w in all_wallets:
        if address == w.address:
            target_address = address
            break
        else:
            raise HTTPException(status_code=404, detail='Wallet not created')
    return templates.TemplateResponse('address.html',
                                      {'request': request, 'address': target_address, 'all_wallets': all_wallets})

