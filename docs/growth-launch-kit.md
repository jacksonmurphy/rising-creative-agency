# Rising growth launch kit

Prepared October 23, 2026. Website changes are on `growth-plan-repairs`; this document does not mean they are deployed. The existing audit remains the baseline. Do not substitute missing metrics with zero.

## Launch sequence

1. Review the revised homepage, `/start-here/`, `/books.html`, `/shop/`, and artwork previews. Confirm the two Gumroad direct links show the intended offers. Check delivery manually using the owner’s chosen test process; no checkout was submitted during implementation.
2. Deploy the reviewed website changes through the existing hosting process. Verify the live URLs and mobile navigation after deployment.
3. In Gumroad Profile → Pages → existing Products section, select **7 Days to Reset Your Heart** and **Rise & Shine**, then save and verify the public storefront. Both were already Published in the audit. This is a visibility repair, not a new product release.
4. Use the corrected brand Instagram account `risingcreativeagency`. Proposed bio destination: `https://risingcreativeagency.com/start-here/?utm_source=instagram&utm_medium=organic_social&utm_campaign=reset_story_test&utm_content=bio`. The page now supplies both the reset and an artwork route. Do not promise a specific print from a general bio link.
5. Begin the four-week experiment only after the live destinations work. Start with two original posts and two or three adapted Pins each week. There is no paid campaign in this plan.

## Four-week working calendar

These are prepared content briefs, not posts already published. Use Jackson’s own images and actual words; do not invent a life event, testimonial, lyric, or page excerpt.

| Week | Story post | Practical post | Pinterest adaptations | Main destination |
|---|---|---|---|---|
| 1 | Introduce the work with the existing line “Songs, books, drawings — all of it began as something private, made for God and himself.” Pair with an actual drawing or studio photo. | Show the free guide cover and explain: 11-page digital guide, seven days, free with optional payment. | One story image; one clear free-guide cover. | Start Here / free guide |
| 2 | Explain in Jackson’s own words the moment behind God, I’m Tired. Include a real music sample only where the account has rights and platform support. | Show a real interior prompt from the guide. Explain how Jackson uses it; no therapeutic promises. | Story-led invitation versus a page-preview invitation. | Same free guide |
| 3 | Share the meaning behind Warrior Lion Heart using the existing artwork. Verify listing 4494325177 immediately before posting. | Show what the buyer receives: digital printable, with actual sizes/file contents copied from the current offer. | Two art Pins: meaning/story and room/use context. Label any mockup and digital delivery accurately. | Exact verified art listing |
| 4 | Return to the more promising story theme with one new personal detail Jackson supplies. | Explain the distinction: free seven-day guide → $5+ 30-day digital journal; Rise and Shine print books are separate. | Repeat the stronger visual format with new source material. | Start Here / paid companion |

### Ready-to-adapt factual captions

**Free guide:** “A little space to begin again. 7 Days to Reset Your Heart is an 11-page digital guide for reflection and a fresh start. It’s free on Gumroad, with an optional contribution. Start with the free guide through the link in the bio.” Pair with the actual cover. Use only after the bio destination is verified.

**Digital continuation:** “If the seven-day reset helped, Rise & Shine offers a longer place to reflect: a 75-page, 30-day digital journal practice, $5+ on Gumroad. This is the digital companion; the Rise and Shine print books are separate editions.” Link to the exact digital offer.

**Art:** “Warrior Lion Heart, by Jackson Murphy. Explore the artwork and the current digital print offer in JacksonsHeartwork on Etsy.” Verify availability and contents before publishing. Add Jackson’s own account of its meaning instead of invented biography.

## Measurement

Use `weekly-scorecard.csv`. Record exact start/end dates and source. Blank means unavailable or not yet collected; zero means the platform actually reported zero. Keep platform windows separate when boundaries differ. Views, impressions, saves, and streams are not unique buyers.

UTM convention for outgoing social links to the website:
- `utm_source=instagram` or `pinterest`
- `utm_medium=organic_social`
- `utm_campaign=reset_story_test` or `art_story_test`
- `utm_content=story_01`, `practice_01`, or another stable, non-personal label.

Do not add UTMs to internal website links: that would obscure acquisition. Existing GA tag G-DNBSVE72WH is preserved; ownership, consent configuration, and reporting access remain unverified. No new tracking service, custom event, or permission was installed. Verify landing-page UTMs in the correct analytics property before relying on attribution. Platform checkout metrics remain the source for orders; an outbound click is not a purchase.

Weekly: compare exposure → outbound clicks → offer views → verified completions/orders. Preserve denominators and small sample sizes. At days 30, 60 and 90 compare complete, non-overlapping 30-day windows. If people do not click, improve the invitation; if people click but do not complete, inspect offer clarity and delivery; if free completions occur without paid sales, evaluate the companion’s fit.

## Decisions still needed

- Which, if any, expired gift listings should incur renewal fees? Select one or two only after fulfillment and margin review.
- Whether and when to publish The Weeping Willow or The Shepherd Who Calls You by Name. Their purchase buttons are removed; no editions were published.
- Exact contents and audio delivery for unavailable art/music bundles. Preview pages no longer promise an MP3 download.
- Remaining artwork IDs marked unverified in `purchase-link-inventory.csv` need current status checks before promotion. The manifest records original destinations for traceability, including removed links.
- Gumroad storefront and social profile changes must be verified in the correct signed-in account. No new account linking or permissions are required by this site change.

## Rollback

The site changes are isolated in one Git branch/commit. Revert that commit to restore the prior website. Account settings, product states, paid renewals and publication are not altered by this commit.
