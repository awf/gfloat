from gfloat import FormatInfo

format_info_binary16 = FormatInfo(
    name="binary16",
    k=16,
    precision=11,
    emax=15,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**10 - 1,
)
format_info_binary32 = FormatInfo(
    name="binary32",
    k=32,
    precision=24,
    emax=127,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**23 - 1,
)

format_info_bfloat16 = FormatInfo(
    name="bfloat16",
    k=16,
    precision=8,
    emax=127,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**7 - 1,
)

format_info_ocp_e5m2 = FormatInfo(
    name="ocp_e5m2",
    k=8,
    precision=3,
    emax=15,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**2 - 1,
)
format_info_ocp_e4m3 = FormatInfo(
    name="ocp_e4m3",
    k=8,
    precision=4,
    emax=8,
    has_nz=True,
    has_infs=False,
    num_high_nans=1,
)


def format_info_p3109(precision) -> FormatInfo:
    name = f"p3109_p{precision}"
    emax = int(2 ** (7 - precision) - 1)

    return FormatInfo(
        name,
        k=8,
        precision=precision,
        emax=emax,
        has_nz=False,
        has_infs=True,
        num_high_nans=0,
    )
