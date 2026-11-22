import pytest
import render.cloud_phase_multiscatter as mod

CASES = [
    ("dual_lobe_hg", (0.3, 0.5)),
    ("multiscatter_compensate", (1, 2)),
    ("optical_depth_segment", (1, 2)),
    ("sun_low_angle", (5.0, 2.0)),
    ("forward_peak", (1, 2)),
    ("back_shadow", (1, 2)),
    ("energy_conservation", (0.8, 1.0)),
    ("phase_anisotropy", (0.6, 0.2)),
    ("step_count", (64, 32)),
    ("shadow_map_blend", (1, 2)),
    ("density_scale", (0.5, 0.2)),
    ("multiple_octave", (1, 2)),
    ("godray_guard", (1, 2)),
    ("tone_stability", (1, 2)),
    ("brightness_metric", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
