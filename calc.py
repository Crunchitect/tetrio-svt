from math import sin, cos, radians

def get_point_in_cir(h, k, theta, r):
    return r * sin(radians(theta)) + h, r * cos(radians(theta)) + k


def right_svt_flash_points(w, h, r, Δ, θ):
    return [
        get_point_in_cir(w // 8 * 5, h * 4 // 3, Δ + 180 + (θ // 2), r),
        get_point_in_cir(w // 8 * 5, h * 4 // 3, Δ + 180 - (θ // 2), r),
        get_point_in_cir(w // 8 * 5, h * 4 // 3, Δ + 180 - (θ // 2), r + (3 * h)),
        get_point_in_cir(w // 8 * 5, h * 4 // 3, Δ + 180 + (θ // 2), r + (3 * h))
    ]


def left_svt_flash_points(w, h, r, Δ, θ):
    return [
        get_point_in_cir(w // 8 * 3, h * 4 // 3, Δ + 180 + (θ // 2), r),
        get_point_in_cir(w // 8 * 3, h * 4 // 3, Δ + 180 - (θ // 2), r),
        get_point_in_cir(w // 8 * 3, h * 4 // 3, Δ + 180 - (θ // 2), r + (3 * h)),
        get_point_in_cir(w // 8 * 3, h * 4 // 3, Δ + 180 + (θ // 2), r + (3 * h))
    ]


def cubic_bezier(p0, p1, p2, p3):
    return lambda t: (
        (1-t) * (1-t) * (1-t) * p0     +
        t     * (1-t) * (1-t) * p1 * 3 +
        t     * t     * (1-t) * p2 * 3 +
        t     * t     * t     * p3     
    )


def lerp(a, b, t):
    return (1 - t) * a + b * t


def double_cubic_bezier(p0, p1, p2, p3):
    return lambda t: (cubic_bezier(p0, p1, p2, p3)((1 - t) * 2)) if t > 0.5 else cubic_bezier(p0, p1, p2, p3)(t * 2)