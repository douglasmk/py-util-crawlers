
class Html():
    @staticmethod
    def table(content:[], html_options):
        response = Html.thead(list(content[0].keys()))
        response += Html.tbody(list(content))

        return Html.tag('table', response, html_options)


    @staticmethod
    def thead(rows:[]):
        return Html.tag('thead', Html.tr(rows, True))


    @staticmethod
    def th(content:str):
        return Html.tag('th', content)


    @staticmethod
    def tbody(rows:[]):
        content = ''
        for row in rows:
            content += Html.tr(row.values())

        return Html.tag('tbody', content)


    @staticmethod
    def tr(itens:[], header:bool = False):
        content = ''
        for item in itens:
            content += Html.th(item) if header else Html.td(item)

        return Html.tag('tr', content)


    @staticmethod
    def td(content:str):
        return Html.tag('td', content)


    @staticmethod
    def tag(tag:str, content:str, html_options:{} = {}):
        return Html.begin_tag(tag, html_options)+content+Html.end_tag(tag)


    @staticmethod
    def begin_tag(tag:str, html_options:{} = {}):
        return '<'+tag+Html.parse_options(html_options)+'>'


    @staticmethod
    def end_tag(tag:str):
        return '</'+tag+'>'


    @staticmethod
    def hr(html_options:{} = {}):
        return '<hr'+Html.parse_options(html_options)+'/>'


    @staticmethod
    def br(html_options:{} = {}):
        return '<br'+Html.parse_options(html_options)+'/>'


    @staticmethod
    def parse_options(html_options:{} = {}):
        return ' '+(' '.join([f'{key}="{value}"' for key, value in html_options.items()])) if html_options else ''
