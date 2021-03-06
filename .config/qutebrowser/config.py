import os
# config.load_autoconfig()

# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
# c.auto_save.interval = 15000
# c.auto_save.session = False
# c.backend = 'webengine'
# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}
# c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #888888, stop:1 #505050)'
# c.colors.completion.category.border.bottom = 'black'
# c.colors.completion.category.border.top = 'black'
# c.colors.completion.category.fg = 'white'
# c.colors.completion.even.bg = '#333333'
# c.colors.completion.fg = ['white', 'white', 'white']
# c.colors.completion.item.selected.bg = '#e8c000'
# c.colors.completion.item.selected.border.bottom = '#bbbb00'
# c.colors.completion.item.selected.border.top = '#bbbb00'
# c.colors.completion.item.selected.fg = 'black'
# c.colors.completion.item.selected.match.fg = '#ff4444'
# c.colors.completion.match.fg = '#ff4444'
# c.colors.completion.odd.bg = '#444444'
# c.colors.completion.scrollbar.bg = '#333333'
# c.colors.completion.scrollbar.fg = 'white'
# c.colors.contextmenu.menu.bg = None
# c.colors.contextmenu.menu.fg = None
# c.colors.contextmenu.selected.bg = None
# c.colors.contextmenu.selected.fg = None
# c.colors.downloads.bar.bg = 'black'
# c.colors.downloads.error.bg = 'red'
# c.colors.downloads.error.fg = 'white'
# c.colors.downloads.start.bg = '#0000aa'
# c.colors.downloads.start.fg = 'white'
# c.colors.downloads.stop.bg = '#00aa00'
# c.colors.downloads.stop.fg = 'white'
# c.colors.downloads.system.bg = 'rgb'
# c.colors.downloads.system.fg = 'rgb'
# c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'
# c.colors.hints.fg = 'black'
# c.colors.hints.match.fg = 'green'
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'
# c.colors.keyhint.fg = '#FFFFFF'
# c.colors.keyhint.suffix.fg = '#FFFF00'
# c.colors.messages.error.bg = 'red'
# c.colors.messages.error.border = '#bb0000'
# c.colors.messages.error.fg = 'white'
# c.colors.messages.info.bg = 'black'
# c.colors.messages.info.border = '#333333'
# c.colors.messages.info.fg = 'white'
# c.colors.messages.warning.bg = 'darkorange'
# c.colors.messages.warning.border = '#d47300'
# c.colors.messages.warning.fg = 'white'
# c.colors.prompts.bg = '#444444'
# c.colors.prompts.border = '1px solid gray'
# c.colors.prompts.fg = 'white'
# c.colors.prompts.selected.bg = 'grey'
# c.colors.statusbar.caret.bg = 'purple'
# c.colors.statusbar.caret.fg = 'white'
# c.colors.statusbar.caret.selection.bg = '#a12dff'
# c.colors.statusbar.caret.selection.fg = 'white'
# c.colors.statusbar.command.bg = 'black'
# c.colors.statusbar.command.fg = 'white'
# c.colors.statusbar.command.private.bg = 'darkslategray'
# c.colors.statusbar.command.private.fg = 'white'
# c.colors.statusbar.insert.bg = 'darkgreen'
# c.colors.statusbar.insert.fg = 'white'
# c.colors.statusbar.normal.bg = 'black'
# c.colors.statusbar.normal.fg = 'white'
# c.colors.statusbar.passthrough.bg = 'darkblue'
# c.colors.statusbar.passthrough.fg = 'white'
# c.colors.statusbar.private.bg = '#666666'
# c.colors.statusbar.private.fg = 'white'
# c.colors.statusbar.progress.bg = 'white'
# c.colors.statusbar.url.error.fg = 'orange'
# c.colors.statusbar.url.fg = 'white'
# c.colors.statusbar.url.hover.fg = 'aqua'
# c.colors.statusbar.url.success.http.fg = 'white'
# c.colors.statusbar.url.success.https.fg = 'lime'
# c.colors.statusbar.url.warn.fg = 'yellow'
# c.colors.tabs.bar.bg = '#555555'
# c.colors.tabs.even.bg = 'darkgrey'
# c.colors.tabs.even.fg = 'white'
# c.colors.tabs.indicator.error = '#ff0000'
# c.colors.tabs.indicator.start = '#0000aa'
# c.colors.tabs.indicator.stop = '#00aa00'
# c.colors.tabs.indicator.system = 'rgb'
# c.colors.tabs.odd.bg = 'grey'
# c.colors.tabs.odd.fg = 'white'
# c.colors.tabs.pinned.even.bg = 'darkseagreen'
# c.colors.tabs.pinned.even.fg = 'white'
# c.colors.tabs.pinned.odd.bg = 'seagreen'
# c.colors.tabs.pinned.odd.fg = 'white'
# c.colors.tabs.pinned.selected.even.bg = 'black'
# c.colors.tabs.pinned.selected.even.fg = 'white'
# c.colors.tabs.pinned.selected.odd.bg = 'black'
# c.colors.tabs.pinned.selected.odd.fg = 'white'
# c.colors.tabs.selected.even.bg = 'black'
# c.colors.tabs.selected.even.fg = 'white'
# c.colors.tabs.selected.odd.bg = 'black'
# c.colors.tabs.selected.odd.fg = 'white'
# c.colors.webpage.bg = 'white'
c.colors.webpage.prefers_color_scheme_dark = True
# c.completion.cmd_history_max_items = 100
# c.completion.delay = 0
c.completion.height = '50%'
# c.completion.min_chars = 1
c.completion.open_categories = ['quickmarks', 'bookmarks', 'history']
# c.completion.quick = True
# c.completion.scrollbar.padding = 2
# c.completion.scrollbar.width = 12
# c.completion.show = 'always'
c.completion.shrink = True
c.completion.timestamp_format = '%d-%m-%Y'
# c.completion.use_best_match = False
# c.completion.web_history.exclude = []
# c.completion.web_history.max_items = -1
c.confirm_quit = ['downloads']
c.content.autoplay = False
# c.content.cache.appcache = True
# c.content.cache.maximum_pages = 0
# c.content.cache.size = None
# c.content.canvas_reading = True
# c.content.cookies.accept = 'all'
# c.content.cookies.store = True
# c.content.default_encoding = 'iso-8859-1'
# c.content.desktop_capture = 'ask'
c.content.dns_prefetch = True
# c.content.frame_flattening = False
# c.content.geolocation = 'ask'
# c.content.headers.accept_language = 'en-US,en;q=0.9'
# c.content.headers.custom = {}
# c.content.headers.do_not_track = True
# c.content.headers.referer = 'same-domain'
# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'
c.content.host_blocking.enabled = True
c.content.host_blocking.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts', 'https://github.com/jmdugan/blocklists/raw/master/corporations/facebook/all-but-whatsapp', 'https://github.com/jmdugan/blocklists/raw/master/corporations/cloudflare/all', 'https://github.com/jmdugan/blocklists/raw/master/corporations/amazon/all', 'https://raw.githubusercontent.com/jmdugan/blocklists/master/corporations/twitter/all', 'https://github.com/jmdugan/blocklists/raw/master/corporations/microsoft/all', 'https://github.com/jmdugan/blocklists/raw/master/corporations/apple/all', 'file:///home/mubashir/.local/share/qutebrowser/custom-host-file']
# c.content.host_blocking.whitelist = ['']
# c.content.hyperlink_auditing = False
# c.content.images = True
# c.content.javascript.alert = True
# c.content.javascript.can_access_clipboard = False
# c.content.javascript.can_close_tabs = False
# c.content.javascript.can_open_tabs_automatically = False
# c.content.javascript.enabled = True
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}
# c.content.javascript.modal_dialog = False
# c.content.javascript.prompt = True
# c.content.local_content_can_access_file_urls = True
# c.content.local_content_can_access_remote_urls = False
# c.content.local_storage = True
# c.content.media_capture = 'ask'
# c.content.mouse_lock = 'ask'
# c.content.mute = False
# c.content.netrc_file = None
c.content.notifications = False
#c.content.pdfjs = False
# c.content.persistent_storage = 'ask'
# c.content.plugins = False
# c.content.print_element_backgrounds = True
# c.content.private_browsing = False
# c.content.proxy = 'system'
# c.content.proxy_dns_requests = True
# c.content.register_protocol_handler = 'ask'
# c.content.site_specific_quirks = True
# c.content.ssl_strict = 'ask'
c.content.user_stylesheets = ['~/.config/qutebrowser/gruvbox-all-sites.css']
# c.content.webgl = True
# c.content.webrtc_ip_handling_policy = 'all-interfaces'
# c.content.windowed_fullscreen = False
# c.content.xss_auditing = False
# c.downloads.location.directory = None
# c.downloads.location.prompt = True
# c.downloads.location.remember = True
# c.downloads.location.suggestion = 'path'
# c.downloads.open_dispatcher = None
c.downloads.position = 'bottom'
c.downloads.remove_finished = 2000
c.editor.command = [os.getenv('TERMINAL', 'st'), "-e", os.getenv('EDITOR', 'vim'), "{file}"]
# c.editor.encoding = 'utf-8'
# c.fonts.completion.category = 'bold default_size default_family'
# c.fonts.completion.entry = 'default_size default_family'
# c.fonts.contextmenu = None
# c.fonts.debug_console = 'default_size default_family'
# c.fonts.default_family = []
# c.fonts.default_size = '10pt'
# c.fonts.downloads = 'default_size default_family'
# c.fonts.hints = 'bold default_size default_family'
# c.fonts.keyhint = 'default_size default_family'
# c.fonts.messages.error = 'default_size default_family'
# c.fonts.messages.info = 'default_size default_family'
# c.fonts.messages.warning = 'default_size default_family'
# c.fonts.prompts = 'default_size sans-serif'
# c.fonts.statusbar = 'default_size default_family'
# c.fonts.tabs = 'default_size default_family'
# c.fonts.web.family.cursive = ''
# c.fonts.web.family.fantasy = ''
# c.fonts.web.family.fixed = ''
# c.fonts.web.family.sans_serif = ''
# c.fonts.web.family.serif = ''
# c.fonts.web.family.standard = ''
# c.fonts.web.size.default = 16
# c.fonts.web.size.default_fixed = 13
# c.fonts.web.size.minimum = 0
# c.fonts.web.size.minimum_logical = 6
# c.hints.auto_follow = 'unique-match'
# c.hints.auto_follow_timeout = 0
# c.hints.border = '1px solid #E3BE23'
# c.hints.chars = 'asdfghjkl'
# c.hints.dictionary = '/usr/share/dict/words'
# c.hints.find_implementation = 'python'
# c.hints.hide_unmatched_rapid_hints = True
# c.hints.leave_on_load = True
# c.hints.min_chars = 1
# c.hints.mode = 'letter'
# c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']
# c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']
# c.hints.scatter = True
# c.hints.selectors = {'all': ['a', 'area', 'textarea', 'select', 'input:not([type="hidden"])', 'button', 'frame', 'iframe', 'img', 'link', 'summary', '[onclick]', '[onmousedown]', '[role="link"]', '[role="option"]', '[role="button"]', '[ng-click]', '[ngClick]', '[data-ng-click]', '[x-ng-click]', '[tabindex]'], 'links': ['a[href]', 'area[href]', 'link[href]', '[role="link"][href]'], 'images': ['img'], 'media': ['audio', 'img', 'video'], 'url': ['[src]', '[href]'], 'inputs': ['input[type="text"]', 'input[type="date"]', 'input[type="datetime-local"]', 'input[type="email"]', 'input[type="month"]', 'input[type="number"]', 'input[type="password"]', 'input[type="search"]', 'input[type="tel"]', 'input[type="time"]', 'input[type="url"]', 'input[type="week"]', 'input:not([type])', 'textarea']}
c.hints.selectors["code"] = [
    # Selects all code tags whose direct parent is not a pre tag
    ":not(pre) > code",
    "pre"
]
# c.hints.uppercase = False
# c.history_gap_interval = 30
# c.input.escape_quits_reporter = True
# c.input.forward_unbound_keys = 'auto'
# c.input.insert_mode.auto_enter = True
# c.input.insert_mode.auto_leave = True
# c.input.insert_mode.auto_load = False
c.input.insert_mode.leave_on_load = False
# c.input.insert_mode.plugins = False
# c.input.links_included_in_focus_chain = True
# c.input.partial_timeout = 5000
# c.input.rocker_gestures = False
# c.input.spatial_navigation = False
# c.keyhint.blacklist = []
# c.keyhint.delay = 500
# c.keyhint.radius = 6
#c.messages.timeout = 2000
# c.new_instance_open_target = 'tab'
# c.new_instance_open_target_window = 'last-focused'
# c.prompt.filebrowser = True
# c.prompt.radius = 8
# c.qt.args = []
# c.qt.force_platform = None
# c.qt.force_platformtheme = None
# c.qt.force_software_rendering = 'none'
# c.qt.highdpi = False
# c.qt.low_end_device_mode = 'auto'
# c.qt.process_model = 'process-per-site-instance'
# c.scrolling.bar = 'when-searching'
# c.scrolling.smooth = False
# c.search.ignore_case = 'smart'
# c.search.incremental = True
# c.session.default_name = None
# c.session.lazy_restore = False
# c.spellcheck.languages = []
# c.statusbar.hide = False
c.statusbar.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
# c.statusbar.position = 'bottom'
c.statusbar.widgets = ['keypress', 'url', 'tabs', 'progress']
# c.tabs.background = False
# c.tabs.close_mouse_button = 'middle'
# c.tabs.close_mouse_button_on_bar = 'new-tab'
# c.tabs.favicons.scale = 1.0
# c.tabs.favicons.show = 'always'
# c.tabs.focus_stack_size = 10
# c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}
# c.tabs.indicator.width = 3
# c.tabs.last_close = 'ignore'
# c.tabs.max_width = -1
# c.tabs.min_width = -1
# c.tabs.mode_on_change = 'normal'
# c.tabs.mousewheel_switching = True
# c.tabs.new_position.related = 'next'
# c.tabs.new_position.stacking = True
# c.tabs.new_position.unrelated = 'last'
# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}
# c.tabs.pinned.frozen = True
# c.tabs.pinned.shrink = True
# c.tabs.position = 'top'
c.tabs.select_on_remove = 'last-used'
c.tabs.show = 'multiple'
# c.tabs.show_switching_delay = 800
# c.tabs.tabs_are_windows = False
# c.tabs.title.alignment = 'left'
# c.tabs.title.format = '{audio}{index}: {current_title}'
# c.tabs.title.format_pinned = '{index}'
# c.tabs.tooltips = True
# c.tabs.undo_stack_size = 100
# c.tabs.width = '20%'
# c.tabs.wrap = True
# c.url.auto_search = 'naive'
c.url.default_page = 'about:blank'
# c.url.incdec_segments = ['path', 'query']
# c.url.open_base_url = False
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}' , 'g': 'https://www.google.com/search?q={}' , 'aw': 'https://wiki.archlinux.org/?search={}', 'yt': 'https://www.youtube.com/results?search_query={}', 'r': 'https://reddit.com/r/{}', 'ka': 'https://kissanime.nz/Search/?s={}'}
c.url.start_pages = ['about:blank']
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
# c.window.hide_decoration = False
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'
# c.zoom.default = '100%'
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
# c.zoom.mouse_divider = 512
# c.zoom.text_only = False
# config.bind("'", 'enter-mode jump_mark')
# config.bind('+', 'zoom-in')
# config.bind('-', 'zoom-out')
# config.bind('.', 'repeat-command')
# config.bind('/', 'set-cmd-text /')
# config.bind(':', 'set-cmd-text :')
# config.bind(';I', 'hint images tab')
# config.bind(';O', 'hint links fill :open -t -r {hint-url}')

# config.bind(';R', 'hint --rapid links window')
# config.bind(';Y', 'hint links yank-primary')
# config.bind(';b', 'hint all tab-bg')
# config.bind(';d', 'hint links download')
# config.bind(';f', 'hint all tab-fg')
# config.bind(';h', 'hint all hover')
# config.bind(';i', 'hint images')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind(';r', 'hint --rapid links tab-bg')
# config.bind(';t', 'hint inputs')
# config.bind(';y', 'hint links yank')
# config.bind('<Alt-1>', 'tab-focus 1')
# config.bind('<Alt-2>', 'tab-focus 2')
# config.bind('<Alt-3>', 'tab-focus 3')
# config.bind('<Alt-4>', 'tab-focus 4')
# config.bind('<Alt-5>', 'tab-focus 5')
# config.bind('<Alt-6>', 'tab-focus 6')
# config.bind('<Alt-7>', 'tab-focus 7')
# config.bind('<Alt-8>', 'tab-focus 8')
# config.bind('<Alt-9>', 'tab-focus -1')
# config.bind('<Alt-m>', 'tab-mute')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-B>', 'scroll-page 0 -1')
# config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
# config.bind('<Ctrl-F5>', 'reload -f')
# config.bind('<Ctrl-F>', 'scroll-page 0 1')
# config.bind('<Ctrl-N>', 'open -w')
# config.bind('<Ctrl-PgDown>', 'tab-next')
# config.bind('<Ctrl-PgUp>', 'tab-prev')
# config.bind('<Ctrl-Q>', 'quit')
# config.bind('<Ctrl-Return>', 'follow-selected -t')
# config.bind('<Ctrl-Shift-N>', 'open -p')
# config.bind('<Ctrl-Shift-T>', 'undo')
# config.bind('<Ctrl-Shift-Tab>', 'nop')
# config.bind('<Ctrl-Shift-W>', 'close')
# config.bind('<Ctrl-T>', 'open -t')
# config.bind('<Ctrl-Tab>', 'tab-focus last')
# config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
# config.bind('<Ctrl-V>', 'enter-mode passthrough')
# config.bind('<Ctrl-W>', 'tab-close')
# config.bind('<Ctrl-X>', 'navigate decrement')
# config.bind('<Ctrl-^>', 'tab-focus last')
# config.bind('<Ctrl-h>', 'home')
# config.bind('<Ctrl-p>', 'tab-pin')
# config.bind('<Ctrl-s>', 'stop')
# config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
# config.bind('<F11>', 'fullscreen')
# config.bind('<F5>', 'reload')
# config.bind('<Return>', 'follow-selected')
# config.bind('<back>', 'back')
# config.bind('<forward>', 'forward')
# config.bind('=', 'zoom')
# config.bind('?', 'set-cmd-text ?')
# config.bind('@', 'run-macro')
# config.bind('B', 'set-cmd-text -s :quickmark-load -t')
# config.bind('D', 'tab-close -o')
# config.bind('F', 'hint all tab')
# config.bind('G', 'scroll-to-perc')
# config.bind('H', 'back')
config.bind('K', 'tab-next')
config.bind('J', 'tab-prev')
# config.bind('L', 'forward')
# config.bind('M', 'bookmark-add')
# config.bind('N', 'search-prev')
# config.bind('O', 'set-cmd-text -s :open -t')
# config.bind('PP', 'open -t -- {primary}')
# config.bind('Pp', 'open -t -- {clipboard}')
# config.bind('R', 'reload -f')
# config.bind('Sb', 'open qute://bookmarks#bookmarks')
# config.bind('Sh', 'open qute://history')
# config.bind('Sq', 'open qute://bookmarks')
# config.bind('Ss', 'open qute://settings')
# config.bind('T', 'tab-focus')
# config.bind('ZQ', 'quit')
# config.bind('ZZ', 'quit --save')
# config.bind('[[', 'navigate prev')
# config.bind(']]', 'navigate next')
# config.bind('`', 'enter-mode set_mark')
# config.bind('ad', 'download-cancel')
# config.bind('b', 'set-cmd-text -s :quickmark-load')
# config.bind('cd', 'download-clear')
# config.bind('co', 'tab-only')
# config.bind('d', 'tab-close')
# config.bind('f', 'hint')
# config.bind('g$', 'tab-focus -1')
# config.bind('g0', 'tab-focus 1')
# config.bind('gB', 'set-cmd-text -s :bookmark-load -t')
# config.bind('gC', 'tab-clone')
# config.bind('gD', 'tab-give')
# config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
# config.bind('gU', 'navigate up -t')
# config.bind('g^', 'tab-focus 1')
# config.bind('ga', 'open -t')
# config.bind('gb', 'set-cmd-text -s :bookmark-load')
# config.bind('gd', 'download')
# config.bind('gf', 'view-source')
# config.bind('gg', 'scroll-to-perc 0')
# config.bind('gi', 'hint inputs --first')
# config.bind('gl', 'tab-move -')
# config.bind('gm', 'tab-move')
# config.bind('go', 'set-cmd-text :open {url:pretty}')
# config.bind('gr', 'tab-move +')
# config.bind('gt', 'set-cmd-text -s :buffer')
# config.bind('gu', 'navigate up')
# config.bind('i', 'enter-mode insert')

# config.bind('h', 'scroll-px -35 0')
# config.bind('j', 'scroll-px 0 35')
# config.bind('k', 'scroll-px 0 -35')
# config.bind('l', 'scroll-px 35 0')

# config.bind('m', 'quickmark-save')
# config.bind('n', 'search-next')
# config.bind('o', 'set-cmd-text -s :open')
# config.bind('pP', 'open -- {primary}')
# config.bind('pp', 'open -- {clipboard}')
# config.bind('q', 'record-macro')
config.unbind('q')
# config.bind('r', 'reload')
# config.bind('sf', 'save')
# config.bind('sk', 'set-cmd-text -s :bind')
# config.bind('sl', 'set-cmd-text -s :set -t')
# config.bind('ss', 'set-cmd-text -s :set')
# config.bind('tIH', 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tIh', 'config-cycle -p -u *://{url:host}/* content.images ;; reload')
# config.bind('tIu', 'config-cycle -p -u {url} content.images ;; reload')
# config.bind('tPH', 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tPh', 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tPu', 'config-cycle -p -u {url} content.plugins ;; reload')
# config.bind('tSH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSu', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
# config.bind('th', 'back -t')
# config.bind('tiH', 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tih', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
# config.bind('tiu', 'config-cycle -p -t -u {url} content.images ;; reload')
# config.bind('tl', 'forward -t')
# config.bind('tpH', 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tph', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tpu', 'config-cycle -p -t -u {url} content.plugins ;; reload')
# config.bind('tsH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsu', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
# config.bind('u', 'undo')
# config.bind('v', 'enter-mode caret')
# config.bind('wB', 'set-cmd-text -s :bookmark-load -w')
# config.bind('wO', 'set-cmd-text :open -w {url:pretty}')
# config.bind('wP', 'open -w -- {primary}')
# config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
# config.bind('wf', 'hint all window')
# config.bind('wh', 'back -w')
# config.bind('wi', 'inspector')
# config.bind('wl', 'forward -w')
# config.bind('wo', 'set-cmd-text -s :open -w')
# config.bind('wp', 'open -w -- {clipboard}')
# config.bind('xO', 'set-cmd-text :open -b -r {url:pretty}')
# config.bind('xo', 'set-cmd-text -s :open -b')
# config.bind('yD', 'yank domain -s')
# config.bind('yM', 'yank inline [{title}]({url}) -s')
# config.bind('yP', 'yank pretty-url -s')
# config.bind('yT', 'yank title -s')
# config.bind('yY', 'yank -s')
# config.bind('yd', 'yank domain')
# config.bind('ym', 'yank inline [{title}]({url})')
# config.bind('yp', 'yank pretty-url')
# config.bind('yt', 'yank title')
# config.bind('yy', 'yank')
# config.bind('{{', 'navigate prev -t')
# config.bind('}}', 'navigate next -t')
config.bind('R', 'restart')
config.bind('xx', 'config-cycle statusbar.hide ;; config-cycle tabs.show multiple never')
config.bind('XX', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/gruvbox-all-sites.css ""')
config.bind('po', 'set-cmd-text -s :open -p')
config.bind('pF', 'hint links run open -p {hint-url}')
config.bind('<Ctrl-Shift-F>', 'hint links spawn --detach mpv {hint-url}')
config.bind('<Ctrl-Shift-T>', 'hint links spawn --detach transadd {hint-url}')
config.bind('<shift-#>', 'hint code userscript code_select.py')
config.bind('<Shift-q>', 'hint links spawn --detach qrgen {hint-url}')
# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
# config.bind('<Escape>', 'leave-mode', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'toggle-selection', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('H', 'scroll left', mode='caret')
# config.bind('J', 'scroll down', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('Y', 'yank selection -s', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('c', 'enter-mode normal', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('o', 'reverse-selection', mode='caret')
# config.bind('v', 'toggle-selection', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')
# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'completion-item-focus --history next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'leave-mode', mode='hint')
# config.bind('<Return>', 'follow-hint', mode='hint')
# config.bind('<Ctrl-E>', 'open-editor', mode='insert')
# config.bind('<Escape>', 'leave-mode', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text -- {primary}', mode='insert')
# config.bind('<Shift-Escape>', 'leave-mode', mode='passthrough')
# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
# config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='register')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
# config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
# config.bind('<Escape>', 'leave-mode', mode='yesno')
# config.bind('<Return>', 'prompt-accept', mode='yesno')
# config.bind('N', 'prompt-accept --save no', mode='yesno')
# config.bind('Y', 'prompt-accept --save yes', mode='yesno')
# config.bind('n', 'prompt-accept no', mode='yesno')
# config.bind('y', 'prompt-accept yes', mode='yesno')



# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova and Daniel Mulford
# Gruvbox dark, hard scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

# base00 = "#1d2021"
base00 = "#282828"
base01 = "#3c3836"
base02 = "#504945"
base03 = "#665c54"
base04 = "#bdae93"
base05 = "#d5c4a1"
base06 = "#ebdbb2"
base07 = "#fbf1c7"
base08 = "#fb4934"
base09 = "#fe8019"
base0A = "#fabd2f"
base0B = "#b8bb26"
base0C = "#8ec07c"
base0D = "#83a598"
base0E = "#d3869b"
base0F = "#d65d0e"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0D

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base01

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base00

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0D

# Top border color of the selected completion item
c.colors.completion.item.selected.border.top = base0D

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0D

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base00

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base0D

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base00

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base05

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0C

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0A

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base00

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base04

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base0E

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base01

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0D

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0B

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base00

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0B

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base00

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base00

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base0D

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base0D

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base00

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base00

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base0D

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base00

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base0D

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = base00
