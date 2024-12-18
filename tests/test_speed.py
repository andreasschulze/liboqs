# SPDX-License-Identifier: MIT

import helpers
import os
import os.path
import pytest
import platform

@helpers.filtered_test
@pytest.mark.parametrize('kem_name', helpers.available_kems_by_name())
def test_kem(kem_name):
    kats = helpers.get_kats("kem")
    if not(helpers.is_kem_enabled_by_name(kem_name)): pytest.skip('Not enabled')
    helpers.run_subprocess( [helpers.path_to_executable('speed_kem'), kem_name, "-f"] )

@helpers.filtered_test
@pytest.mark.parametrize('sig_name', helpers.available_sigs_by_name())
def test_sig(sig_name):
    kats = helpers.get_kats("sig")
    if not(helpers.is_sig_enabled_by_name(sig_name)): pytest.skip('Not enabled')
    helpers.run_subprocess( [helpers.path_to_executable('speed_sig'), sig_name, "-f"])

@helpers.filtered_test
@pytest.mark.parametrize('sig_stfl_name', helpers.available_sig_stfls_by_name())
def test_sig(sig_stfl_name):
    kats = helpers.get_kats("sig_stfl")
    if not(helpers.is_sig_stfl_enabled_by_name(sig_stfl_name)):
        pytest.skip('Not enabled')
    elif sig_stfl_name.find("_10")==-1 and sig_stfl_name.find("H10")==-1:
        pytest.skip('Test skipped')
    else:
        helpers.run_subprocess( [helpers.path_to_executable('speed_sig_stfl'), sig_stfl_name, "-f"])

if __name__ == "__main__":
    import sys
    pytest.main(sys.argv)
