import FinanceDataReader as fdr
import requests
from bs4 import BeautifulSoup

# 엑셀 파일 URL
url = "https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&pageIndex=1&currentPageSize=3000&comAbbrv=&beginIndex=&orderMode=3&orderStat=D&isurCd=&repIsuSrtCd=&searchCodeType=&marketType=stockMkt&searchType=06&industry=&fiscalYearEnd=all&comAbbrvTmp=&location=all"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        # HTML 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 종목코드가 있는 td 태그 찾기
        stock_code_cells = soup.find_all('td', attrs={'style': "mso-number-format:'@';text-align:center;"})
        
        # 종목코드 추출
        stock_codes = [cell.text.strip() for cell in stock_code_cells]
        
        # 결과 출력
        print("추출된 종목코드:")
        for code in stock_codes:
            print(code)
            
        # 필요한 경우 DataFrame으로 변환
        import pandas as pd
        df = pd.DataFrame(stock_codes, columns=['종목코드'])
        print("\nDataFrame 형태:")
        print(df.head())
            
    else:
        print(f"Error: 파일 다운로드 실패. Status code: {response.status_code}")
        
except Exception as e:
    print(f"오류 발생: {e}")

    