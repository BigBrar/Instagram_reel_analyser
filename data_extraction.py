from bs4 import BeautifulSoup
import json
from collections import Counter
from time import sleep

def extract_urls(soup):
    href_url = soup.findAll('a',{'class':'x1i10hfl'}) # .get('href')
    all_urls = []
    for url in href_url:
        if url.get('href').startswith('/reel/'):all_urls.append(url.get('href'))
    return all_urls

def convert_original_numbers(num):
    num = num.replace('K','')
    try:
        num+='000'
        num = int(num)
    except:
        num+='000'
        num = float(num)
    return num

def extract_urls1(soup):
    href_url = soup.findAll('a', {'class': 'x1i10hfl'})
    all_urls = []
    seen_urls = set()  # Use a set to keep track of seen URLs
    for url in href_url:
        if url.get('href').startswith('/reel/') and url.get('href') not in seen_urls:
            all_urls.append(url.get('href'))
            seen_urls.add(url.get('href'))  # Add the URL to the set
    return all_urls



def extract_likes(soup,urls):
    likes_divs = soup.findAll('div',{'class':'_aajz'})
    processed_div = set()
    likes_array = []
    views_array = []
    comments_array = []
    skipped = 0
    zeroes=0
    index=0
    for div in likes_divs:
        if div not in processed_div:
            soup2 = BeautifulSoup(str(div),'html.parser')
            all_span = soup2.findAll('span')
            index+=1
            likes_array.append(all_span[0].text)
            
            comments_array.append(all_span[3].text)
            
            try:
                views_array.append(all_span[6].text)
            except:
                views_array.append(0)
                zeroes+=1

            processed_div.add(div)
        else:
            skipped+=1
   
    print(f'Number of processed divs {index}')
    print(f'Number of skipped divs {skipped}')
    print(f'Number of empty views divs {zeroes}')
    
    all_results = []
    length = len(likes_array)
    seen_urls = set()
    index = 0
    for i in range(length):
        index+=1
        if len(all_results) >1:
            for result in all_results:
                if index > len(urls):
                    print(len(urls) - length)
                    print(f'Length of the likes -{length}')
                    print(f'Length of current likes{len(all_results)}')
                    return all_results
                if urls[i] == result['reel_url']:
                    pass
                else:
                    if urls[i] not in seen_urls:
                        seen_urls.add(urls[i]) 
                        try:
                            all_results.append({'likes':likes_array[i],'comments':comments_array[i],'views':views_array[i],'reel_url':urls[i]})            
                            print(f"We added {urls[i]}")
                        except:
                            pass
        else:
            all_results.append({'likes':likes_array[i],'comments':comments_array[i],'views':views_array[i],'reel_url':urls[i]})
    
    print(json.dumps(all_results,indent=4))
    return all_results
    

def convert_numeric_values(data):
    for entry in data:
        for key in ['likes', 'comments', 'views']:
            value = entry[key]
            if 'K' in value:
                entry[key] = int(float(value.replace('K', '')) * 1000)
            elif 'M' in value:
                entry[key] = int(float(value.replace('M', '')) * 1000000)
            else:
                entry[key] = int(value.replace(',', ''))
    return data

def get_top_reels(data):
    # Convert likes, comments, and views to integers for proper sorting
    for item in data:
        item['likes'] = int(item['likes'])
        item['comments'] = int(item['comments'])
        item['views'] = int(item['views'])
    
    # Sort data by likes, comments, and views
    top_liked = sorted(data, key=lambda x: x['likes'], reverse=True)[:-1]
    top_commented = sorted(data, key=lambda x: x['comments'], reverse=True)[:-1]
    top_viewed = sorted(data, key=lambda x: x['views'], reverse=True)[:-1]
    
    # Extract the top 3 items for each category
    result = {
        'top_liked': [{'likes': item['likes'], 'reel_url': item['reel_url']} for item in top_liked],
        'top_commented': [{'comments': item['comments'], 'reel_url': item['reel_url']} for item in top_commented],
        'top_viewed': [{'views': item['views'], 'reel_url': item['reel_url']} for item in top_viewed]
    }
    result = json.dumps(result,indent=4)
    return result

def start_extractor(html_page):
    soup = BeautifulSoup(html_page,'html.parser')

    #extracting all the links
    urls = extract_urls1(soup)
    # #extracting likes - 
    raw_data = extract_likes(soup,urls)
    print("Writing data to file ")
    final_data = json.dumps(raw_data,indent=4)
    return final_data
