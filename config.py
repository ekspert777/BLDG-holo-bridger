import random

'''

     delay - delay between wallets
     mode  -  0 - your chains (need to fill chain and to) ; 1 - search nft in all chains and sending it if it founded in your choosen network

     avax   /   bsc   /   polygon

     chain - from chain
     to - to chain (or random mode - random.choice(['your chain','your chain']) 
     api - need moralis api https://admin.moralis.io/settings#secret-keys
     
'''

delay = (10, 600)
mode = 0
chain = ''        #   avax   /   bsc   /   polygon  /  opti
to = ''  #or ['your chain','your chain']
api = ''

info = {'avax':('https://snowtrace.io/tx/','https://rpc.ankr.com/avalanche'),
        'polygon':('https://polygonscan.com/tx/','https://polygon-rpc.com'),
        'bsc':('https://bscscan.com/tx/','https://bscrpc.com'),
        'opti':('https://optimistic.etherscan.io/tx/','https://optimism.publicnode.com')}
