from library_.config import Config
import xlrd
# path = Config.DATA_PATH

class ReadExcel:

    def read_test_data(self,sheetname):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(sheetname)
        columns = worksheet.ncols
        print(columns)
        rows = worksheet.get_rows()
        header=next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self,sheetname):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(sheetname)
        rows = worksheet.get_rows()
        header = next(rows)
        d = {}

        for row in rows:
            d[row[0].value] = (row[1].value,row[2].value)
        return d


