# bupt-bingo
## Start(Server)
```bash
export SECRET_KEY="随机字符串，用于 JWT 加密"
cd Server
pip install -r requirements.txt
python init_club.py
python init_invite_code.py
bash Server.sh
```

## Start(Web)
```bash
cd Web
npm install
npm run build
```