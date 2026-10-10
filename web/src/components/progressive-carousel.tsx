"use client";

import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  useRef,
  ReactNode,
  FC,
} from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { cx } from "@/components/ui";

interface ProgressSliderContextType {
  active: string;
  progress: number;
  handleButtonClick: (value: string) => void;
  nextSlide: () => void;
  prevSlide: () => void;
  vertical: boolean;
}

interface ProgressSliderProps {
  children: ReactNode;
  duration?: number;
  fastDuration?: number;
  vertical?: boolean;
  activeSlider: string;
  sliderValues?: string[];
  className?: string;
}

interface SliderContentProps {
  children: ReactNode;
  className?: string;
}

interface SliderWrapperProps {
  children: ReactNode;
  value: string;
  className?: string;
}

interface ProgressBarProps {
  children: ReactNode;
  className?: string;
}

interface SliderBtnProps {
  children: ReactNode;
  value: string;
  className?: string;
  progressBarClass?: string;
}

const ProgressSliderContext = createContext<
  ProgressSliderContextType | undefined
>(undefined);

export const useProgressSliderContext = (): ProgressSliderContextType => {
  const context = useContext(ProgressSliderContext);
  if (!context) {
    throw new Error(
      "useProgressSliderContext must be used within a ProgressSlider"
    );
  }
  return context;
};

export const ProgressSlider: FC<ProgressSliderProps> = ({
  children,
  duration = 6000,
  fastDuration = 350,
  vertical = false,
  activeSlider,
  sliderValues: explicitValues,
  className,
}) => {
  const [active, setActive] = useState<string>(activeSlider);
  const [progress, setProgress] = useState<number>(0);
  const [isFastForward, setIsFastForward] = useState<boolean>(false);
  const frame = useRef<number>(0);
  const firstFrameTime = useRef<number>(0);
  const targetValue = useRef<string | null>(null);
  const [sliderValues, setSliderValues] = useState<string[]>(explicitValues ?? []);
  const [isPaused, setIsPaused] = useState<boolean>(false);

  useEffect(() => {
    if (explicitValues && explicitValues.length > 0) {
      setSliderValues(explicitValues);
      return;
    }

    const childrenArray = React.Children.toArray(children);
    const contentChild = childrenArray.find(
      (child) =>
        React.isValidElement(child) &&
        (child.type === SliderContent || (child.props as { children?: ReactNode })?.children)
    ) as React.ReactElement<{ children?: ReactNode }> | undefined;

    if (contentChild && contentChild.props?.children) {
      const values = React.Children.toArray(contentChild.props.children)
        .map((child) =>
          React.isValidElement(child) ? ((child.props as { value?: string }).value as string) : ""
        )
        .filter(Boolean);
      if (values.length > 0) {
        setSliderValues(values);
      }
    }
  }, [children, explicitValues]);

  useEffect(() => {
    if (sliderValues.length === 0 || isPaused) return;

    firstFrameTime.current = typeof window !== "undefined" ? performance.now() : 0;

    const animate = (now: number) => {
      const currentDuration = isFastForward ? fastDuration : duration;
      const elapsedTime = now - firstFrameTime.current;
      const timeFraction = elapsedTime / currentDuration;

      if (timeFraction <= 1) {
        setProgress(
          isFastForward
            ? progress + (100 - progress) * timeFraction
            : timeFraction * 100
        );
        frame.current = requestAnimationFrame(animate);
      } else {
        if (isFastForward) {
          setIsFastForward(false);
          if (targetValue.current !== null) {
            setActive(targetValue.current);
            targetValue.current = null;
          }
        } else {
          const currentIndex = sliderValues.indexOf(active);
          const nextIndex = (currentIndex + 1) % sliderValues.length;
          setActive(sliderValues[nextIndex]);
        }
        setProgress(0);
        firstFrameTime.current = performance.now();
      }
    };

    frame.current = requestAnimationFrame(animate);

    return () => {
      if (typeof window !== "undefined") {
        cancelAnimationFrame(frame.current);
      }
    };
  }, [sliderValues, active, isFastForward, isPaused, duration, fastDuration, progress]);

  const handleButtonClick = (value: string) => {
    if (value !== active) {
      const elapsedTime = performance.now() - firstFrameTime.current;
      const currentProgress = (elapsedTime / duration) * 100;
      setProgress(currentProgress);
      targetValue.current = value;
      setIsFastForward(true);
      firstFrameTime.current = performance.now();
    }
  };

  const nextSlide = () => {
    if (sliderValues.length === 0) return;
    const currentIndex = sliderValues.indexOf(active);
    const nextIndex = (currentIndex + 1) % sliderValues.length;
    handleButtonClick(sliderValues[nextIndex]);
  };

  const prevSlide = () => {
    if (sliderValues.length === 0) return;
    const currentIndex = sliderValues.indexOf(active);
    const prevIndex = (currentIndex - 1 + sliderValues.length) % sliderValues.length;
    handleButtonClick(sliderValues[prevIndex]);
  };

  return (
    <ProgressSliderContext.Provider
      value={{ active, progress, handleButtonClick, nextSlide, prevSlide, vertical }}
    >
      <div
        className={cx("relative group", className)}
        onMouseEnter={() => setIsPaused(true)}
        onMouseLeave={() => setIsPaused(false)}
      >
        {children}
      </div>
    </ProgressSliderContext.Provider>
  );
};

export const SliderContent: FC<SliderContentProps> = ({
  children,
  className,
}) => {
  return <div className={cx("relative overflow-hidden", className)}>{children}</div>;
};

export const SliderWrapper: FC<SliderWrapperProps> = ({
  children,
  value,
  className,
}) => {
  const { active } = useProgressSliderContext();
  const isSelected = active === value;

  return (
    <div
      className={cx(
        "transition-all duration-500 ease-out",
        isSelected
          ? "opacity-100 scale-100 relative z-10 block pointer-events-auto"
          : "opacity-0 scale-98 absolute inset-0 -z-10 pointer-events-none hidden",
        className
      )}
      aria-hidden={!isSelected}
    >
      {children}
    </div>
  );
};

export const SliderBtnGroup: FC<ProgressBarProps> = ({
  children,
  className,
}) => {
  return <div className={cx("", className)}>{children}</div>;
};

export const SliderBtn: FC<SliderBtnProps> = ({
  children,
  value,
  className,
  progressBarClass,
}) => {
  const { active, progress, handleButtonClick, vertical } =
    useProgressSliderContext();

  const isSelected = active === value;

  return (
    <button
      type="button"
      className={cx(
        "relative text-left transition-all duration-300",
        isSelected
          ? "opacity-100 ring-2 ring-primary/60 bg-surface shadow-md border-primary/40"
          : "opacity-60 hover:opacity-90 bg-surface/50 border-border",
        className
      )}
      onClick={() => handleButtonClick(value)}
    >
      {children}
      <div
        className="absolute inset-0 overflow-hidden -z-10 rounded-[inherit]"
        role="progressbar"
        aria-valuenow={isSelected ? progress : 0}
      >
        <span
          className={cx(
            "absolute left-0 top-0 transition-none",
            progressBarClass ?? "bg-primary/20 h-full"
          )}
          style={{
            [vertical ? "height" : "width"]: isSelected ? `${progress}%` : "0%",
            height: vertical ? (isSelected ? `${progress}%` : "0%") : "100%",
          }}
        />
      </div>
    </button>
  );
};

export function SliderNavControls({ className }: { className?: string }) {
  const { prevSlide, nextSlide } = useProgressSliderContext();

  return (
    <div className={cx("flex items-center gap-2", className)}>
      <button
        type="button"
        onClick={prevSlide}
        aria-label="Slide anterior"
        className="grid h-9 w-9 place-items-center rounded-xl border border-border bg-surface text-muted transition hover:bg-surface-2 hover:text-text cursor-pointer active:scale-95 shadow-xs"
      >
        <ChevronLeft className="h-5 w-5" />
      </button>
      <button
        type="button"
        onClick={nextSlide}
        aria-label="Próximo slide"
        className="grid h-9 w-9 place-items-center rounded-xl border border-border bg-surface text-muted transition hover:bg-surface-2 hover:text-text cursor-pointer active:scale-95 shadow-xs"
      >
        <ChevronRight className="h-5 w-5" />
      </button>
    </div>
  );
}
