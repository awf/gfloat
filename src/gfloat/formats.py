from gfloat import FormatInfo

#: FormatInfo for IEEE-754 Binary32 format
format_info_binary32 = FormatInfo(
    name="binary32",
    k=32,
    precision=24,
    emax=127,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**23 - 1,
)

#: FormatInfo for IEEE-754 Binary16 format
format_info_binary16 = FormatInfo(
    name="binary16",
    k=16,
    precision=11,
    emax=15,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**10 - 1,
)

#: FormatInfo for Google BFloat16 format
format_info_bfloat16 = FormatInfo(
    name="bfloat16",
    k=16,
    precision=8,
    emax=127,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**7 - 1,
)

#: FormatInfo for OCP E5M2 format
format_info_ocp_e5m2 = FormatInfo(
    name="ocp_e5m2",
    k=8,
    precision=3,
    emax=15,
    has_nz=True,
    has_infs=True,
    num_high_nans=2**2 - 1,
)

#: FormatInfo for OCP E4M3 format
format_info_ocp_e4m3 = FormatInfo(
    name="ocp_e4m3",
    k=8,
    precision=4,
    emax=8,
    has_nz=True,
    has_infs=False,
    num_high_nans=1,
)


def format_info_p3109(p: int) -> FormatInfo:
    """
    FormatInfo for P3109 P{p} formats

    :param p: Precision in bits
    :type p: int

    :return: FormatInfo class describing the format
    :rtype: FormatInfo

    :raise ValueError: If p is not in 1..7
    """
    if p < 1 or p > 8:
        raise ValueError(f"P3109 format not defined for p={p}")

    name = f"p3109_p{p}"
    emax = int(2 ** (7 - p) - 1)

    return FormatInfo(
        name,
        k=8,
        precision=p,
        emax=emax,
        has_nz=False,
        has_infs=True,
        num_high_nans=0,
    )
