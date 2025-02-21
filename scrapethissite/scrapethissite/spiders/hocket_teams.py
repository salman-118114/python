import scrapy


class HocketTeamsSpider(scrapy.Spider):
    name = "hocket_teams"
    allowed_domains = ["scrapethissite.com"]
    
    def start_requests(self):

        for page in range(1,25):
            yield scrapy.Request(url=f"https://www.scrapethissite.com/pages/forms/?page_num={page}",callback=self.parse)  

    def parse(self, response):
        
        block_name = response.xpath("//tr[@class='team']")


        for each_block in block_name:
            team_name = each_block.xpath(".//td[@class='name']/text()").get()
            team_year = each_block.xpath(".//td[@class='year']/text()").get()
            team_wins = each_block.xpath(".//td[@class='wins']/text()").get()
            team_losses = each_block.xpath(".//td[@class='losses']/text()").get()
        
            yield {
                
                'team_name' : (team_name or '').replace("\n", "").strip(),
                'team_year' : (team_year or '').replace("\n", "").strip(),
                'team_wins' :(team_wins or '').replace("\n", "").strip(),
                'team_losses' : (team_losses or '').replace("\n", "").strip()
            }