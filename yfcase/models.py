from django.conf import settings
from django.db import models
from django.urls import reverse

class Case(models.Model):
	casenumber = models.CharField(u"案號",max_length=100)
	city = models.CharField(u"縣市",max_length=20)
	township = models.CharField(u"鄉鎮區",max_length=20)
	section = models.CharField(u"段",max_length=20)
	small_section = models.CharField(u"小段",max_length=20)
	other_address = models.CharField(u"地址",max_length=200)
	first_surveydate = models.DateField(u"初勘日",auto_now=False, auto_now_add=False)
	other_surveydate = models.DateField(u"覆勘日",auto_now=False, auto_now_add=False)
	survey_remark = models.CharField(u"勘查備註",max_length=100,blank=True, null=True)
	survey_decision = models.CharField(u"會勘決議",max_length=100,blank=True, null=True)
	final_decision = models.CharField(u"最終決定",max_length=100,blank=True, null=True)
	deputy_director1 = models.CharField(u"副署人員1",max_length=100,blank=True, null=True)
	deputy_director2 = models.CharField(u"副署人員2",max_length=100,blank=True, null=True)
	deputy_director3 = models.CharField(u"副署人員3",max_length=100,blank=True, null=True)
	foreclosure_announcement_link= models.CharField(u"法拍公告連結",max_length=100,blank=True, null=True)
	foreclosure_announcement_text= models.CharField(u"法拍公告內容",max_length=100,blank=True, null=True)
	object_photos_link= models.CharField(u"物件照片連結",max_length=100,blank=True, null=True)
	object_photos_text= models.CharField(u"物件照片內容",max_length=100,blank=True, null=True)
	registration_market_price_link= models.CharField(u"實價登錄市價連結",max_length=100,blank=True, null=True)
	registration_market_price_text= models.CharField(u"實價登錄市價內容",max_length=100,blank=True, null=True)
	registration_map_link= models.CharField(u"實價登錄地圖連結",max_length=100,blank=True, null=True)
	registration_map_text= models.CharField(u"實價登錄地圖內容",max_length=100,blank=True, null=True)
	registration_phot_link= models.CharField(u"實價登錄照片連結",max_length=100,blank=True, null=True)
	registration_phot_text= models.CharField(u"實價登錄照片內容",max_length=100,blank=True, null=True)
	foreclosure_record_link= models.CharField(u"拍賣記錄連結",max_length=100,blank=True, null=True)
	foreclosure_record_text= models.CharField(u"拍賣記錄內容",max_length=100,blank=True, null=True)
	auctionday1= models.CharField(u"拍賣日1",max_length=100,blank=True, null=True)
	auctionday2= models.CharField(u"拍賣日2",max_length=100,blank=True, null=True)
	auctionday3= models.CharField(u"拍賣日3",max_length=100,blank=True, null=True)
	auctionday4= models.CharField(u"拍賣日4",max_length=100,blank=True, null=True)
	floorprice1= models.CharField(u"底價1",max_length=100,blank=True, null=True)
	floorprice2= models.CharField(u"底價2",max_length=100,blank=True, null=True)
	floorprice3= models.CharField(u"底價3",max_length=100,blank=True, null=True)
	floorprice4= models.CharField(u"底價4",max_length=100,blank=True, null=True)
	click1= models.CharField(u"點閱1",max_length=100,blank=True, null=True)
	click2= models.CharField(u"點閱2",max_length=100,blank=True, null=True)
	click3= models.CharField(u"點閱3",max_length=100,blank=True, null=True)
	click4= models.CharField(u"點閱4",max_length=100,blank=True, null=True)
	monitor1= models.CharField(u"監控1",max_length=100,blank=True, null=True)
	monitor2= models.CharField(u"監控2",max_length=100,blank=True, null=True)
	monitor3= models.CharField(u"監控3",max_length=100,blank=True, null=True)
	monitor4= models.CharField(u"監控4",max_length=100,blank=True, null=True)
	occupyneighbouringland= models.CharField(u"1.建物坐落是否無占用鄰地",max_length=100,blank=True, null=True)
	register= models.CharField(u"2.建物是否無未保存登記建物",max_length=100,blank=True, null=True)
	parkingspace= models.CharField(u"3.大樓是否有停車位(機車/汽車)",max_length=100,blank=True, null=True)
	managementfee= models.CharField(u"4.大樓公寓是否有無積欠管理費",max_length=100,blank=True, null=True)
	occupy= models.CharField(u"5.有無出租或出借或佔用",max_length=100,blank=True, null=True)
	leak= models.CharField(u"6.建物是否無嚴重漏水現象",max_length=100,blank=True, null=True)
	easyparking= models.CharField(u"7.建物前或附近是否停車方便",max_length=100,blank=True, null=True)
	railway= models.CharField(u"8.是否鄰近捷運站或台鐵站",max_length=100,blank=True, null=True)
	vegetablemarket= models.CharField(u"9.是否鄰近菜市場",max_length=100,blank=True, null=True)
	store= models.CharField(u"10.是否鄰近大賣場",max_length=100,blank=True, null=True)
	school= models.CharField(u"11.是否鄰近學校",max_length=100,blank=True, null=True)
	park= models.CharField(u"12.是否鄰近公園",max_length=100,blank=True, null=True)
	postoffice= models.CharField(u"13.是否鄰近郵局或常用機關",max_length=100,blank=True, null=True)
	mainroad= models.CharField(u"14.是否鄰近幹道",max_length=100,blank=True, null=True)
	waterandpowerfailure= models.CharField(u"15.是否斷水斷電",max_length=100,blank=True, null=True)
	goodvision= models.CharField(u"16.建物採光視野是否良好",max_length=100,blank=True, null=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		blank=True, 
		null=True,
	)

	def __str__(self):
		return self.casenumber

	def get_absolute_url(self):
		return reverse('case_detail', args=[str(self.id)])

class Land(models.Model):
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	landnumber = models.CharField(u"地號",max_length=100	,blank=True, null=True)
	landurl = models.CharField(u"謄本",max_length=100,blank=True,null=True)
	landarea = models.DecimalField(u"地坪(平方公尺)",max_digits=7, decimal_places=2,blank=True,null=True)
	landholdingpointperson = models.IntegerField(u"個人持分",default=0,blank=True,null=True)
	landholdingpointall = models.IntegerField(u"所有持分",default=0,blank=True,null=True)

	def __str__(self):
		return self.landnumber


class Build(models.Model):
	# BUILDTYPE_CHOICES = [
	# 	('1公寓(5樓含以下無電梯)','1公寓(5樓含以下無電梯)'),
	# 	('2透天厝','2透天厝'),
	# 	('3店面(店舖)','3店面(店舖)'),
	# 	('4辦公商業大樓','4辦公商業大樓'),
	# 	('5住宅大樓(11層含以上有電梯)','5住宅大樓(11層含以上有電梯)'),
	# 	('6華廈(10層含以下有電梯)','6華廈(10層含以下有電梯)'),
	# 	('7套房(1房(1廳)1衛)','7套房(1房(1廳)1衛)'),
	# 	('8工廠','9廠辦','8工廠','9廠辦'),
	# 	('10農舍','10農舍'),
	# 	('11倉庫','11倉庫'),
	# 	('Z其他等型態','Z其他等型態')
	# ]

	# USEAREA_CHOICES = [
	# 	("第一種住宅區","第一種住宅區"),
	# 	("第二種住宅區","第二種住宅區"),
	# 	("第三種住宅區","第三種住宅區"),
	# 	("第四種住宅區","第四種住宅區"),
	# 	("第一種商業區","第一種商業區"),
	# 	("第二種商業區","第二種商業區"),
	# 	("第三種商業區","第三種商業區"),
	# 	("第四種商業區","第四種商業區"),
	# 	("第二種工業區","第二種工業區"),
	# 	("第三種工業區","第三種工業區"),
	# 	("行政區","行政區"),
	# 	("文教區","文教區"),
	# 	("倉庫區","倉庫區"),
	# 	("風景區","風景區"),
	# 	("農業區","農業區"),
	# 	("保護區","保護區"),
	# 	("行水區","行水區"),
	# 	("保存區","保存區"),
	# 	("特定專用區","特定專用區")
	# ]
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	buildnumber = models.CharField(u"建號",max_length=100,blank=True, null=True)
	buildurl = models.CharField(u"謄本",max_length=100,blank=True,null=True)
	buildarea = models.DecimalField(u"建坪(平方公尺)",max_digits=7, decimal_places=2,blank=True,null=True)
	buildholdingpointperson = models.IntegerField(u"個人持分",default=0,blank=True,null=True)
	buildholdingpointall = models.IntegerField(u"所有持分",default=0,blank=True,null=True)
	buildtype = models.CharField(u"建物型使用",max_length=20,blank=True,null=True)
	usearea = models.CharField(u"使用分區",max_length=100,blank=True, null=True)


	def __str__(self):
		return self.buildnumber


class Personnal(models.Model):
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	creditor = models.BooleanField(u"債務人",blank=True, null=True)
	debtor = models.BooleanField(u"債權人",blank=True, null=True)
	landowner = models.BooleanField(u"土地共有人",blank=True, null=True)
	buildowner = models.BooleanField(u"建物共有人",blank=True, null=True)
	name = models.CharField(u"姓名",max_length=100	,blank=True, null=True)
	identitycard = models.CharField(u"身分証",max_length=100	,blank=True, null=True)
	birthday = models.DateField(u"生日",auto_now=False, auto_now_add=False)
	address = models.CharField(u"位址",max_length=100,blank=True,null=True)
	telphone = models.CharField(u"市話",max_length=100,blank=True,null=True)
	mobile = models.CharField(u"手機",max_length=100,blank=True,null=True)
	remark = models.CharField(u"備註",max_length=100,blank=True,null=True)
	landholdingpointperson = models.IntegerField(u"個人持分",default=0,blank=True,null=True)
	landholdingpointall = models.IntegerField(u"所有持分",default=0,blank=True,null=True)

	def __str__(self):
		return self.name


class Objectbuild(models.Model):
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	address = models.CharField(u"物件地址",max_length=100,blank=True, null=True)
	objectbuildurl = models.CharField(u"謄本",max_length=100,blank=True,null=True)
	totalprice = models.IntegerField(u"總價",default=0,blank=True,null=True)
	buildarea = models.DecimalField(u"建坪(平方公尺)",max_digits=7, decimal_places=2,blank=True,null=True)
	house_age = models.DecimalField(u"屋齡",max_digits=7, decimal_places=2,blank=True,null=True)
	unit = models.CharField(u"單位",max_length=100,blank=True, null=True)
	floorheight = models.CharField(u"樓高",max_length=100,blank=True, null=True)

	def __str__(self):
		return self.address




