#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Marc George
#                 Dave Hunt <dhunt@mozilla.com>
#                 Joel Andersson <janderssn@gmail.com>
#                 Teodosia Pop <teodosia.pop@softvision.ro>
#                 Tobias Markus <tobbi.bugs@googlemail.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****


from unittestzero import Assert

from addons_site import AddonsHomePage
import pytest
xfail = pytest.mark.xfail


class TestThemes:

    def test_that_themes_can_be_sorted_by_name(self, testsetup):
        """ Test for Litmus 11727, 4839 """
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        amo_themes_page.click_sort_by("name")
        addons = amo_themes_page.addon_names
        addons_set = set(addons)
        Assert.equal(len(addons), len(addons_set), "There are duplicates in the names")
        addons_orig = addons
        addons.sort()
        [Assert.equal(addons_orig[i], addons[i]) for i in xrange(len(addons))]
        amo_themes_page.page_forward()
        addons = amo_themes_page.addon_names
        addons_set = set(addons)
        Assert.equal(len(addons), len(addons_set), "There are duplicates in the names")
        addons_orig = addons
        addons.sort()
        [Assert.equal(addons_orig[i], addons[i]) for i in xrange(len(addons))]

    def test_that_themes_can_be_sorted_by_updated_date(self, testsetup):
        """ test for litmus 11638 """
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        amo_themes_page.click_sort_by("updated")
        addons = amo_themes_page.addon_names
        addons_set = set(addons)
        Assert.equal(len(addons), len(addons_set), "There are duplicates in the names")
        updated_dates = amo_themes_page.addon_updated_dates
        Assert.is_sorted_descending(updated_dates)
        amo_themes_page.page_forward()
        updated_dates.extend(amo_themes_page.addon_updated_dates)
        Assert.is_sorted_descending(updated_dates)

    def test_that_themes_can_be_sorted_by_created_date(self, testsetup):
        """ test for litmus 11638 """
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        amo_themes_page.click_sort_by("created")
        addons = amo_themes_page.addon_names
        addons_set = set(addons)
        Assert.equal(len(addons), len(addons_set), "There are duplicates in the names")
        created_dates = amo_themes_page.addon_created_dates
        Assert.is_sorted_descending(created_dates)
        amo_themes_page.page_forward()
        created_dates.extend(amo_themes_page.addon_created_dates)
        Assert.is_sorted_descending(created_dates)

    def test_that_themes_can_be_sorted_by_popularity(self, testsetup):
        """ test for litmus 11638 """
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        amo_themes_page.click_sort_by("popular")
        addons = amo_themes_page.addon_names
        addons_set = set(addons)
        Assert.equal(len(addons), len(addons_set), "There are duplicates in the names")
        downloads = amo_themes_page.addon_download_number
        Assert.is_sorted_descending(downloads)
        amo_themes_page.page_forward()
        downloads.extend(amo_themes_page.addon_download_number)
        Assert.is_sorted_descending(downloads)

    def test_that_themes_loads_themes_landing_page(self, testsetup):
        """test for litmus 15339"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        url_current_page = amo_themes_page.get_url_current_page()
        Assert.true(url_current_page.endswith("/themes/"))

    def test_that_clicking_on_theme_name_loads_its_detail_page(self, testsetup):
        """test for litmus 15363"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        addon_name = amo_themes_page.addon_names[0]
        amo_theme_page = amo_themes_page.click_on_first_addon()
        Assert.equal(addon_name, amo_theme_page.addon_title)

    def test_that_themes_page_has_correct_title(self, testsetup):
        """test for litmus 15340"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        expected_title = "Most Popular :: Themes :: Add-ons for Firefox"
        Assert.equal(expected_title, amo_themes_page.page_title)

    def test_themes_page_breadcrumb(self, testsetup):
        """test for litmus 15344"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        expected_breadcrumb = "Add-ons for Firefox Themes"
        Assert.equal(expected_breadcrumb, amo_themes_page.themes_breadcrumb)

    def test_that_clicking_on_a_subcategory_loads_expected_page(self, testsetup):
        """test for litmus 15949"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        selected_category = amo_themes_page.themes_category
        amo_category_page = amo_themes_page.click_on_first_category()
        Assert.equal(selected_category, amo_category_page.title)

    def test_themes_subcategory_page_breadcrumb(self, testsetup):
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        selected_category = amo_themes_page.themes_category
        amo_category_page = amo_themes_page.click_on_first_category()
        expected_breadcrumb = "Add-ons for Firefox Themes %s" % selected_category
        Assert.equal(expected_breadcrumb, amo_category_page.breadcrumb)

    def test_that_counters_show_the_same_number_of_themes(self, testsetup):
        """test for litmus 15345"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        Assert.equal(amo_themes_page.top_counter, amo_themes_page.bottom_counter)

    def test_that_themes_is_listed_as_a_category(self, testsetup):
        """ test for litmus 15338"""
        amo_home_page = AddonsHomePage(testsetup)
        Assert.true(amo_home_page.has_category("Themes"))

    def test_that_most_popular_link_is_selected_by_default(self, testsetup):
        """ test for litmus 15348"""
        amo_home_page = AddonsHomePage(testsetup)
        amo_themes_page = amo_home_page.click_themes()
        Assert.true(amo_themes_page.is_most_popular_category_selected)
        Assert.equal(amo_themes_page.current_sort, "Downloads")
