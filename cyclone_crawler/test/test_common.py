import unittest
import pytest
from connection import pg_conn
from db import init_table, insert_data, close_connection
from app.crawler import get_active_cyclones

html = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n\t"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n
<html xmlns="http://www.w3.org/1999/xhtml">\n
  <head>\n
    <!-- Start of /templates/html_header.asp (was actually above with\n        DOCTYPE). -->\n\n
    <link rel="Shortcut Icon" href="/favicon.ico" type="image/x-icon" />\n\n
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />\n
    <meta http-equiv="Content-Language" content="en-us" />\n
    <meta name="robots" content="all" />\n
    <meta http-equiv="imagetoolbar" content="false" />\n
    <meta name="MSSmartTagsPreventParsing" content="true" />\n\n
    <!-- Start of /templates/google_analytics_code.asp -->\n
    <!-- Start of Google Analytics Code -->\n
    <script>\n          (function(i,s,o,g,r,a,m){
        i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n          })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n\n          ga(\'create\', \'UA-250602-6\', \'auto\');\n          ga(\'send\', \'pageview\');\n\n        </script>\n
    <!-- End of Google Analytics Code -->\n
    <!-- End of /templates/google_analytics_code.asp -->\n\n
    <!-- End of /templates/html_header.asp -->\n\n
    <!-- Start of section that was specific to each page. -->\n\n
    <meta name="author" content="RAMMB" />\n
    <meta name="Copyright" content="Copyright (c) RAMMB" />\n
    <meta name="description" content="" />\n
    <meta name="keywords" content="" />\n\n
    <style type="text/css" media="all">\n            @import "/css/rammb.css";
      \n            @import "/css/tc_realtime.css";
      \n        </style>\n\n
    <script language="JavaScript" type="text/javascript" src="/javascript/includes.js">
    </script>\n\n        \n    \n
    <title>RAMMB: TC Real-Time: Currently Active Tropical Cyclones
    </title>\n        \n\n\n\n        \n\n\n
  </head>\n
  <body>\n
    <!-- End of section that was specific to each page. -->\n\n
    <!-- Start of /templates/rammb_header.asp -->\n\n
    <!-- Start wrapper -->\n
    <div id="wrapper">\n\n
      <!--\t<p style="color: red; font-weight: bold;">The transition to the new web server is almost complete. Data for most products has been updating during the transition, and will appear on the new site today, July 14th. Thank you for your patience.</p>\n        -->\n
      <!-- Start header -->\n
      <div id="rammb_header">\n
        <p class="access">
          <a href="#content">Skip navigation
          </a>
        </p>\n\n
        <a href="http://rammb.cira.colostate.edu/">
          <img id="rammb" src="/images/rammb_text_logo.jpg" alt="RAMMB: Regional and Mesoscale Meteorology Branch logo" />
        </a>\n\n
        <a href="http://www.cira.colostate.edu/">
          <img id="cira" src="/images/cira_logo_165.png" alt="CIRA: Cooperative Institute for Research in the Atmosphere logo" />
        </a>\n\n
        <a href="http://www.nesdis.noaa.gov/">
          <img id="nesdis" src="/images/nesdis_banner.gif" width="440" height="50" alt="NESDIS: NOAA Environmental Satellite, Data, and Information Service logo" />
        </a>\n\n
        <p id="textlinks">
          <a href="http://www.orbit.nesdis.noaa.gov/star/CoRP_index.php">Cooperative Research Program (CoRP)
          </a> |
          <a href="http://www.orbit.nesdis.noaa.gov/star/">Center for Satellite Applications and Research (STAR)
          </a>
        </p>\n
        <!--\n                <p style="text-align: center"><span style="color: red">Announcement:</span> Please visit out new web application, <a href="http://rammb-slider.cira.colostate.edu">SLIDER</a>, for every pixel of real-time GOES-16 and Himawari-8 imagery.</p>\n                -->\n
      </div>\n
      <!-- End header -->\n
      <!-- End of /templates/rammb_header.asp -->\n\n\n\n
      <h2>Currently Active Tropical Cyclones
      </h2>\n
      <!--            <h2>RAMMB: TC Real-Time: Currently Active Tropical Cyclones</h2>-->\n\n
      <!-- Start of /products/tc_realtime/header.asp. -->\n\n
      <!-- Start sidebar -->\n
      <div id="sidebar">\n
        <ul class="list_level_1">\n
          <!-- <li><a href="http://rammb.cira.colostate.edu/products/tc_realtime">Home</a></li> -->\n
          <li>
            <a href="/tc_realtime/">Current Active Cyclones
            </a>
          </li>\n
          <li>
            <span class="list_heading_span">Archive
            </span>\n
            <ul>\n                            \n
              <li>
                <a href="season.asp?storm_season=2021">2021 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2020">2020 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2019">2019 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2018">2018 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2017">2017 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2016">2016 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2015">2015 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2014">2014 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2013">2013 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2012">2012 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2011">2011 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2010">2010 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2009">2009 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2008">2008 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2007">2007 Season
                </a>
              </li>\n                            \n
              <li>
                <a href="season.asp?storm_season=2006">2006 Season
                </a>
              </li>\n                            \n
            </ul>\n
          </li>\n
          <li>
            <a href="about.asp">Additional Information
            </a>
          </li>\n
          <li>
            <a href="links.asp">Additional Links
            </a>
          </li>\n
        </ul>\n
      </div>\n
      <!-- End sidebar -->\n\n
      <!-- End of /products/tc_realtime/header.asp. -->\n\n\n
      <!-- Start main content -->\n
      <div id="content">\n\n
        <!-- Start of Body - ENTER PAGE CONTENTS HERE -->\n\n\n            \n    \n\t\t
        <div class="basin_storms">\n
          <h3>Atlantic
          </h3>\n\t\t\t
          <ul>\n                \n                    \n
            <li>\n
              <a\n                                href="storm.asp?storm_identifier=al902020">AL902020 -  INVEST\n
                <img src="/tc_realtime/products/storms/2020al90/4kmirimg/2020al90_4kmirimg_202012010115.gif" />\n
                </a>\n
            </li>\n                    \n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\t\t
        <div class="basin_storms">\n
          <h3>Eastern Pacific
          </h3>\n\t\t\t
          <ul>\n                \n
            <li>No Currently Active Cyclones
            </li>\n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\t\t
        <div class="basin_storms">\n
          <h3>Central Pacific
          </h3>\n\t\t\t
          <ul>\n                \n
            <li>No Currently Active Cyclones
            </li>\n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\t\t
        <div class="basin_storms">\n
          <h3>Western Pacific
          </h3>\n\t\t\t
          <ul>\n                \n                    \n
            <li>\n
              <a\n                                href="storm.asp?storm_identifier=wp952020">WP952020 -  INVEST\n
                <img src="/tc_realtime/products/storms/2020wp95/4kmirimg/2020wp95_4kmirimg_202012010110.gif" />\n
                </a>\n
            </li>\n                    \n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\t\t
        <div class="basin_storms">\n
          <h3>North Indian Ocean
          </h3>\n\t\t\t
          <ul>\n                \n                    \n
            <li>\n
              <a\n                                href="storm.asp?storm_identifier=io982020">IO982020 -  INVEST\n
                <img src="/tc_realtime/products/storms/2020io98/4kmirimg/2020io98_4kmirimg_202012010115.gif" />\n
                </a>\n
            </li>\n                    \n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\t\t
        <div class="basin_storms">\n
          <h3>Southern Hemisphere
          </h3>\n\t\t\t
          <ul>\n                \n                    \n
            <li>\n
              <a\n                                href="storm.asp?storm_identifier=sh952021">SH952021 -  INVEST\n
                <img src="/tc_realtime/products/storms/2021sh95/4kmirimg/2021sh95_4kmirimg_202012010115.gif" />\n
                </a>\n
            </li>\n                    \n                \n\t\t\t
          </ul>\n\t\t
        </div>\n    \n\n\n\n
        <!--\n        <div class="container">\n            \n    \n                <h1>Currently Active Tropical Cyclones - Flask Super Example</h1>\n            \n\n            <h2>This is part of my base template</h2>\n            <br>\n            <br>\n            <h2>This is part of my base template</h2>\n            <br>\n            <div class="footer">\n                \n                    Watch! This will be added to my base and child templates using the super powerful super block!\n                    <br>\n                    <br>\n                    <br>\n                \n            </div>\n        </div>\n\n\n-->\n\n
        <!-- End of Body - STOP ENTERING PAGE CONTENTS HERE -->\n\n
      </div>\n
      <!-- End main content -->\n\n
      <!-- Start of /templates/rammb_footer.asp. -->\n\n
      <!-- Start footer -->\n
      <div id="rammb_footer">\n
        <div style="float: left;">\n
          <a href="/resources/site_map.asp">Site Map
          </a> -\n
          <a href="/resources/experimental_products_disclaimer.asp">Experimental Products Disclaimer
          </a>\n
        </div>\n
        <div style="float: right;">\n
          <a href="http://www.noaa.gov/privacy.html" title="privacy statement">Privacy Policy
          </a> -\n
          <a href="http://www.noaa.gov/disclaimer.html" title="disclaimer">Disclaimer
          </a> -\n
          <a href="http://www.cio.noaa.gov/services_programs/info_quality.html">Information Quality
          </a>\n
        </div>\n
        <div style="clear: both; float: left; width: 350px;">\n
          <a href="http://www.doc.gov/">US Dept of Commerce
          </a> -\n
          <a href="http://www.noaa.gov/">NOAA
          </a> -\n
          <a href="http://www.nesdis.noaa.gov/">NESDIS
          </a> -\n
          <a href="http://www.orbit.nesdis.noaa.gov/star/">STAR
          </a> -\n
          <a href="http://www.orbit.nesdis.noaa.gov/star/CoRP_index.php">CoRP
          </a>\n
        </div>\n
        <div style="clear: right; float: right;">\n                    Problems or questions?\n
          <a href="mailto:Debra.Molenar%40noaa.gov">Contact the webmaster
          </a>.\n
        </div>\n
        <div style="clear: left; float: left; width: 350px;">\n                    This page verifies as:\n
          <a href="http://validator.w3.org/check/referer">XHTML
          </a>,\n
          <a href="http://jigsaw.w3.org/css-validator/check/referer">CSS
          </a>,\n                    Section 508\n
        </div>\n
        <div style="clear: right; float: right;">\n
          <a href="http://rammb.cira.colostate.edu/">RAMMB Home - http://rammb.cira.colostate.edu/
          </a>\n
        </div>\n
      </div>\n
      <!-- End footer -->\n\n
    </div>\n
    <!-- End wrapper -->\n\n\n\n\n
  </body>\n
</html>\n
<!-- End of /templates/rammb_footer.asp. -->
'''


result = ["('AL902020','INVEST','null','null','Atlantic','storm.asp?storm_identifier=al902020','/tc_realtime/products/storms/2020al90/4kmirimg/2020al90_4kmirimg_202012010115.gif', '2020-12-01 07:29:33.034088')",
 "('WP952020','INVEST','null','null','Western Pacific','storm.asp?storm_identifier=wp952020','/tc_realtime/products/storms/2020wp95/4kmirimg/2020wp95_4kmirimg_202012010110.gif', '2020-12-01 07:29:33.034320')",
 "('IO982020','INVEST','null','null','North Indian Ocean','storm.asp?storm_identifier=io982020','/tc_realtime/products/storms/2020io98/4kmirimg/2020io98_4kmirimg_202012010115.gif', '2020-12-01 07:29:33.034444')",
 "('SH952021','INVEST','null','null','Southern Hemisphere','storm.asp?storm_identifier=sh952021','/tc_realtime/products/storms/2021sh95/4kmirimg/2021sh95_4kmirimg_202012010115.gif', '2020-12-01 07:29:33.034566')"]

def test_crawler():
