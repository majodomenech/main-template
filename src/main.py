import redflagbpm

from bbg.updateDET import update_instruments, update_cashflows

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    isin_list = ['ARPCDB320099', 'ARARGE3209Z1', 'USP989MJBE04', 'US040114HS26', 'ARBYMA300018']
    update_instruments(bpm, isin_list)
    update_cashflows(bpm)
