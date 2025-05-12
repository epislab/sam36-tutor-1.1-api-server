from com.epislab.models.crime_service import CrimeService
from com.epislab.models.dataset import Dataset


class CrimeController:
    dataset = Dataset()
    service = CrimeService()
    def modeling(self, *args):
        this = self.service.preprocess(*args)
        # self.print_this(this)
        return this
    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. cctv 의 type \n {type(this.cctv)} ')
        print(f'2. cctv 의 column \n {this.cctv.columns} ')
        print(f'3. cctv 의 상위 5개 행\n {this.cctv.head()} ')
        print(f'4. cctv 의 null 의 개수\n {this.cctv.isnull().sum()}개')
        print(f'5. crime 의 type \n {type(this.crime)}')
        print(f'6. crime 의 column \n {this.crime.columns}')
        print(f'7. crime 의 상위 5개 행\n {this.crime.head()}개')
        print(f'8. crime 의 null 의 개수\n {this.crime.isnull().sum()}개')
        print(f'5. pop 의 type \n {type(this.pop)}')
        print(f'6. pop 의 column \n {this.pop.columns}')
        print(f'7. pop 의 상위 5개 행\n {this.pop.head()}개')
        print(f'8. pop 의 null 의 개수\n {this.pop.isnull().sum()}개')
        print('*' * 100)