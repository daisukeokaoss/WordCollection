# -*- coding: utf-8 -*-
from DataToConstructSourceCode  import DataToConstructSource


class MedicalWordURLStore:	


	def ReturnURLArray(self):
		ReturnArray = []
		aaArray = [u'「あ」行の言葉',
				   'http://ejje.weblio.jp/category/healthcare/eigky/aa']
		other = ['http://ejje.weblio.jp/category/healthcare/eigky/aa/2',
		           'http://ejje.weblio.jp/category/healthcare/eigky/aa/3',
		           'http://ejje.weblio.jp/category/healthcare/eigky/aa/4',
		           'http://ejje.weblio.jp/category/healthcare/eigky/aa/5',
		           'http://ejje.weblio.jp/category/healthcare/eigky/aa/6',
		           'http://ejje.weblio.jp/category/healthcare/eigky/aa/7']
		ReturnArray.extend(aaArray)
		return ReturnArray
	"""	iiArray = [u'「い」行の言葉',
					'http://ejje.weblio.jp/category/healthcare/eigky/ii',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/2',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/3',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/4',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/5',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/6',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/7',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/8',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ii/9']
		ReturnArray.extend(iiArray)
		uuArray  = [u'「う」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/uu',
		           'http://ejje.weblio.jp/category/healthcare/eigky/uu/2',
		           'http://ejje.weblio.jp/category/healthcare/eigky/uu/3',
		           'http://ejje.weblio.jp/category/healthcare/eigky/uu/4']
		ReturnArray.extend(uuArray)
		eeArray  = [u'「え」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/ee',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ee/2',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ee/3',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ee/4']
		ReturnArray.extend(eeArray)
		ooArray  = [u'「お」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/oo',
		            'http://ejje.weblio.jp/category/healthcare/eigky/oo/2',
		            'http://ejje.weblio.jp/category/healthcare/eigky/oo/3',
		            'http://ejje.weblio.jp/category/healthcare/eigky/oo/4']
		ReturnArray.extend(ooArray)
		kaArray   = [u'「か」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/ka',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/2',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/3',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/4',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/5',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/6',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/7',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/8',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/9',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/10',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/11',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/12',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/13',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/14',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/15',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/16',
		             'http://ejje.weblio.jp/category/healthcare/eigky/ka/17']
		ReturnArray.extend(kaArray)
		kiArray  = [u'「き」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/ki',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/2',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/3',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/4',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/5',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/6',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/7',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/8',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/9',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/10',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/11',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/12',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/13',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ki/14']
		ReturnArray.extend(kiArray)
		kuArray = [u'「く」行の言葉',
					'http://ejje.weblio.jp/category/healthcare/eigky/ku',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ku/2',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ku/3',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ku/4']
		ReturnArray.extend(kuArray)
		KeArray  = [u'「け」行の言葉',
						'http://ejje.weblio.jp/category/healthcare/eigky/ke',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/2',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/3',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/4',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/5',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/6',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/7',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/8',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/9',
		            'http://ejje.weblio.jp/category/healthcare/eigky/ke/10']
		ReturnArray.extend(KeArray)
		KoArray = [u'「こ」行の言葉',
					'http://ejje.weblio.jp/category/healthcare/eigky/ko',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/2',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/3',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/4',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/5',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/6',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/7',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/8',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/9',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/10',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/11',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/12',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/13',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/14',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/15',
		           'http://ejje.weblio.jp/category/healthcare/eigky/ko/16',
		           ]
		"""
		